#!"C:\Users\lak.DJH.000\OneDrive - djhhadsten.dk\Modul 2.1\04 Opgaver\01 OPGAVE Python kursus Pycharm\.idea\VirtualEnvironment\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==40.8.0','console_scripts','easy_install-3.8'
__requires__ = 'setuptools==40.8.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('setuptools==40.8.0', 'console_scripts', 'easy_install-3.8')()
    )
