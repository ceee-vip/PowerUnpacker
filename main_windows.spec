# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


pf_foldr= f"{os.getcwd()}\\venv\\Lib\\site-packages\\PySide6\\plugins\\platforms\\"

a = Analysis(['main.py'],
             pathex=[f"{os.getcwd()}"],
             binaries=[],
             datas=[(pf_foldr+'qwindows.dll', 'platforms\\'),
             (pf_foldr+'qdirect2d.dll', 'platforms\\'),
             (pf_foldr+'qoffscreen.dll', 'platforms\\'),
             (pf_foldr+'qminimal.dll', 'platforms\\')
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
