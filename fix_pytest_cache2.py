import os
import shutil
import subprocess
from pathlib import Path

p = Path(r"c:\Users\bediw\Documents\Studi\Python projet\.pytest_cache")
print('path:', p)
print('exists:', p.exists())
print('is_dir:', p.is_dir())

try:
    takeown = subprocess.run([
        'takeown',
        '/f',
        str(p),
        '/r',
        '/d',
        'O',
    ], capture_output=True, text=True)
    print('takeown returncode:', takeown.returncode)
    print(takeown.stdout)
    print(takeown.stderr)
except Exception as e:
    print('takeown exception:', type(e).__name__, e)

try:
    username = os.environ.get('USERNAME', 'bediw')
    domain = os.environ.get('USERDOMAIN', 'YOUSSEF')
    user = f'{domain}\\{username}'
    icacls = subprocess.run([
        'icacls',
        str(p),
        '/grant',
        f'{user}:F',
        '/t',
    ], capture_output=True, text=True)
    print('icacls returncode:', icacls.returncode)
    print(icacls.stdout)
    print(icacls.stderr)
except Exception as e:
    print('icacls exception:', type(e).__name__, e)

try:
    shutil.rmtree(p)
    print('removed')
except Exception as e:
    print('remove exception:', type(e).__name__, e)
