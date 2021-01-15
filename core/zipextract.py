import multiprocessing
import os
import queue
import zipfile
import time
import threading

import rarfile

from core.core import Configuration


class PwdParser(threading.Thread):
    config = None
    my_sign = None
    startTime = None
    # 判断线程是否需要终止
    finish = False

    pwd_queue = None
    z_file = None

    def __init__(self, my_sign, config: Configuration):
        super().__init__()
        self.config = config
        self.finish = False
        self.my_sign = my_sign
        self.startTime = time.time()
        self.pwd_queue = multiprocessing.Queue(1000)
        if self.config.zip_file.lower().endswith('zip'):
            self.z_file = zipfile.ZipFile(self.config.zip_file, 'r')
        else:
            self.z_file = rarfile.RarFile(self.config.zip_file, 'r')

    def run(self):
        # start consumer

        for n in range(self.config.thread_num):
            v = threading.Thread(target=self.consumer)
            v.start()
            print("start", n)
        # start producer
        self.do_main()
        # self.z_file.close()

    def consumer(self):
        while not self.finish:
            try:
                pwd = self.pwd_queue.get_nowait()
                self.my_sign.sign_log.emit(f"{pwd}")
                self.extract_one(pwd, self.z_file)
                self.my_sign.sign_correct_passwrod.emit(f"{pwd}")
                self.finish = True
                break
            except Exception as e:

                # self.my_sign.sign_zip_label_digital.emit(pwd, 9999)
                pass
        print("exit")

    def extract_one(self, pwd, file):
        one = file.infolist()[0]
        file.extract(one, pwd=pwd.encode('utf8'))
        if os.path.exists(one.filename):
            os.remove(one.filename)

    def do_main(self):
        for n in range(9999):
            pwd = f"{n}"
            if not self.finish:
                self.pwd_queue.put(pwd)
                self.my_sign.sign_zip_label_digital.emit(n, 9999)

        while True:
            time.sleep(1)
            if self.pwd_queue.empty():
                self.finish = True
                print("return")
                return
