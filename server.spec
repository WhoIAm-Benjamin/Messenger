# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
path_import = 'D:\\Python\\Lib\\site-packages'

a = Analysis(['server.py'],
             pathex=['D:\\Programming\\Messenger'],
             binaries=[],
             datas=[],
             hiddenimports=[path_import + 'PySide2.QtWidgets', path_import + 'socket', 'D:\Programming\Messenger\design_messenger.py'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False, version = 'version_server.rc' )
