# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

project_dir = Path(SPECPATH)
a = Analysis(
    [str(project_dir / 'main.py')],
    pathex=[],
    binaries=[],
    datas=[
        (str(project_dir / "cjk-tables" / "*.txt"), "cjk-tables"),
        (str(project_dir / "readme.txt"), "."),
        (str(project_dir / "LICENSE"), "."),
        (str(project_dir / "appicon.ico"), "."),
        (str(project_dir / "GenYoGothicTW-R.ttf"), "."),
        (str(project_dir / "cjk-char-header.ttf"), "."),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon=str(project_dir / "appicon.ico"),
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # Keep runtime data beside the executable for the existing resource lookup.
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)

if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='main.app',
        icon=None,
        bundle_identifier=None,
        info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
        },
    )
