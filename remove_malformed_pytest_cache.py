import shutil
from pathlib import Path

root = Path(r"c:\Users\bediw\Documents\Studi\Python projet")
bad = root / "'.pytest_cache'"
print('target:', bad)
print('exists:', bad.exists())
print('is_dir:', bad.is_dir())

try:
    shutil.rmtree(bad)
    print('removed')
except Exception as e:
    print(type(e).__name__, e)
