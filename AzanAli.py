#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Azan.so brand.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Azan.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Azan/blob/main/Azan.cpython-310.so?raw=true -o Jutt.so')
        from Azan import reg
        reg()
    else:
        from Azan import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('Azan.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Azan/blob/main/Azan.cpython-310.so?raw=true -o brand.so')
        from Azan import reg
        reg()
    else:
        from Azan import reg
        reg()
