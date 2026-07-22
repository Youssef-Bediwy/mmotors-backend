import shutil
from pathlib import Path

p = Path(r"c:\Users\bediw\Documents\Studi\Python projet\.pytest_cache")
print('path:', p)
print('exists:', p.exists())
print('is_dir:', p.is_dir())

try:
    shutil.rmtree(p)
    print('removed')
except Exception as e:
    print(type(e).__name__, e)
