# -*- mode: python ; coding: utf-8 -*-
#pyinstaller -w -D rpa.spec

block_cipher = None

SETUP_DIR = 'C:\\Users\\Charlie\\Desktop\\py\\'

a = Analysis(['rpa.py','kaka.py','bom.py','Algo.py'],
             pathex=['C:\\Users\\Charlie\\Desktop\\py'],
             binaries=[('logo.ico','.'),('rpa.ini','.')],
             datas=[(SETUP_DIR+'file','file'),(SETUP_DIR+'pic','pic')],
             hiddenimports=['constant.const'],
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
          name='索威尔RPA',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon='logo.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='索威尔RPA',icon='logo.ico')
