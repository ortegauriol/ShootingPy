# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ShootKey.py'],
    pathex=[],
    binaries=[],
    datas=[('Correct.jpg', '.'), ('Bedroom Cup L.jpg', '.'), ('Bedroom Cup R.jpg', '.'), ('Bedroom Keys L.jpg', '.'), ('Bedroom Keys R.jpg', '.'), ('Bedroom Machete L.jpg', '.'), ('Bedroom Machete R.jpg', '.'), ('Bedroom Phone L.jpg', '.'), ('Bedroom Phone R.jpg', '.'), ('Bedroom Pistol L.jpg', '.'), ('Bedroom Pistol R.jpg', '.'), ('Bedroom Rifle L.jpg', '.'), ('Bedroom Rifle R.jpg', '.'), ('Bedroom.jpg', '.'), ('Break.jpg', '.'), ('Dining Room.jpg', '.'), ('Garage.jpg', '.'), ('Incorrect.jpg', '.'), ('Instructions.jpg', '.'), ('Kitchen.jpg', '.'), ('Lounge.jpg', '.'), ('Trigger.jpg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ShootKey',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
