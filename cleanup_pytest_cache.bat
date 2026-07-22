@echo off
"C:\Users\bediw\AppData\Local\Programs\Python\Python314\python.exe" -c "import os, shutil; p=r'C:\Users\bediw\Documents\Studi\Python projet\.pytest_cache'; print('exists', os.path.exists(p)); print('is_dir', os.path.isdir(p)); shutil.rmtree(p); print('removed')"
