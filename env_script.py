import os
import platform

os_name = platform.system()
if os_name == 'Windows':
    os.system('python3 -m venv env && .\\env\\Scripts\\activate && pip install -r requirements.txt')
    print('Create env... [OK]')