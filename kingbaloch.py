import os, platform

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from Kb import bnsbuy

    bnsbuy()

elif bit == '32bit':

    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
