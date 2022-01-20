import os
import platform


def launch_env():
    os_name = platform.system()
    if os_name == 'Windows':
        os.system('.\\env\\Scripts\\activate.bat')
    print('Launch virtual env... [OK]')


def install_flake8():
    if os.system('pip list --disable-pip-version-check | findstr flake-html'):
        print('Flake8 is already install.. [OK]')
    else:
        os.system('pip install flake8-html')
        print('Install flake8... [OK]')


def create_report():
    os.system(
        'flake8 --format=html --htmldir=flake-report --max-line-length=120 --exclude=env,.vscode')
    print('Report flake8... [OK]')


launch_env()
install_flake8()
create_report()
