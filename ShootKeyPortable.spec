# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ShootKeyPortable.py'],
    pathex=[],
    binaries=[],
    datas=[('Break_keyboard.jpeg', '.'), ('Correct.jpg', '.'), ('Incorrect.jpg', '.'), ('Instructions.jpeg', '.'), ('Trigger.jpg', '.'), ('Bedroom.jpg', '.'), ('Lounge.jpg', '.'), ('Kitchen.jpg', '.'), ('Bedroom Pistol L.jpg', '.'), ('Bedroom Pistol R.jpg', '.'), ('Bedroom Rifle L.jpg', '.'), ('Bedroom Rifle R.jpg', '.'), ('Lounge Pistol L.jpg', '.'), ('Lounge Pistol R.jpg', '.'), ('Lounge Rifle L.jpg', '.'), ('Lounge Rifle R.jpg', '.'), ('Kitchen Pistol L.jpg', '.'), ('Kitchen Pistol R.jpg', '.'), ('Kitchen Rifle L.jpg', '.'), ('Kitchen Rifle R.jpg', '.'), ('Bedroom Keys L.jpg', '.'), ('Bedroom Keys R.jpg', '.'), ('Bedroom Phone L.jpg', '.'), ('Bedroom Phone R.jpg', '.'), ('Lounge Keys L.jpg', '.'), ('Lounge Keys R.jpg', '.'), ('Lounge Phone L.jpg', '.'), ('Lounge Phone R.jpg', '.'), ('Kitchen Keys L.jpg', '.'), ('Kitchen Keys R.jpg', '.'), ('Kitchen Phone L.jpg', '.'), ('Kitchen Phone R.jpg', '.')],
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
    name='ShootKeyPortable',
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
