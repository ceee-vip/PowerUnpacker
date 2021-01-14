import os
import zipfile
import time
import threading

from core.core import Configuration


class PwdParser(threading.Thread):
    config = None
    my_sign = None
    startTime = None
    # 判断线程是否需要终止
    flag = True

    def __init__(self, my_sign, config: Configuration):
        super().__init__()
        self.config = config
        self.my_sign = my_sign
        self.startTime = time.time()

    def run(self):
        self.do_main()

    def extract_one(self, pwd, file):
        one = file.infolist()[0]
        file.extract(one, pwd=pwd.encode('utf8'))
        if os.path.exists(one.filename):
            os.remove(one.filename)

    def do_main(self):
        z_file = zipfile.ZipFile(self.config.zip_file, 'r')
        # 开始尝试
        for number in range(1, 9999):
            if self.flag is True:
                ###xxxxxxxx修改
                time.sleep(0.001)
                try:
                    self.extract_one(f"{number}", z_file)
                    self.my_sign.sign_correct_passwrod.emit(f"{number}")
                    print(f"Success Password: {number}")
                    self.flag = True
                    break
                except:
                    self.my_sign.sign_zip_label_digital.emit(number, 9999)
