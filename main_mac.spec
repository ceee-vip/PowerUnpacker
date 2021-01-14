# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

pf_foldr= f"{os.getcwd()}/venv/lib/python3.7/site-packages/PySide6/Qt/plugins/platforms/"

a = Analysis(['main.py'],
             pathex=['/Users/Leo/JetBrainWorkspace/PycharmProjects/PowerUnpacker'],
             binaries=[],
             datas=[(pf_foldr+'libqcocoa.dylib', 'Pyside6/plugins/platforms'),
                 (pf_foldr+'libqminimal.dylib', 'Pyside6/plugins/platforms'),
                 (pf_foldr+'libqoffscreen.dylib', 'Pyside6/plugins/platforms')
                 ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon='images/favicon.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
app = BUNDLE(coll,
             name='main.app',
             icon=None,
             bundle_identifier=None)
