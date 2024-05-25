# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/fevzi/OneDrive/Área de Trabalho/Faculdade/Soluções/Andrefy (Player de Música)/py/AndPlayer.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/fevzi/OneDrive/Área de Trabalho/Faculdade/Soluções/Andrefy (Player de Música)', 'Andrefy (Player de Música)/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AndPlayer',
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
    icon=['C:\\Users\\fevzi\\OneDrive\\Área de Trabalho\\Faculdade\\Soluções\\Andrefy (Player de Música)\\imagens\\icon.ico'],
)
