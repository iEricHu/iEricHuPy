# EHNetwork.py
# <PyDecl: Module Init, Setup DebugMode>
import EHDebug

clsEHDebug = EHDebug.EHDebugClass()
c_blnEHDebugMode = clsEHDebug.p_EHDebugMode
# </PyDecl: Module Init>

import platform
import socket  # fnNetworkSocketPing
import subprocess
import urllib.request  # fnNetworkURLLibOpen

import requests  # fnNetworkRequestPing
from ping3 import ping  # fnNetworkPing

# <PyDecl: RunTime>
if c_blnEHDebugMode: print('DebugMode Entry: EHNetwork.py !')
# </PyDecl: RunTime>
def fnNetworkPing(strIP):
    sngResponse = ping(strIP)
    if not sngResponse is None: return True

def fnNetworkRequestPing(strIP)->(bool, str):
    try:
        response = requests.get(strIP, timeout=5)
        return True, response
    except requests.ConnectionError:
        return False

def fnNetworkSocketPing(strIP, intPort):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect((strIP, intPort))
        return True
    except socket.error:
        return False
    finally:
        sock.close()

def fnNetworkURLLibOpen(strWebAddr):
    try:
        urllib.request.urlopen(strWebAddr)
        return True
    except urllib.error.URLError:
        return False

def fnNetworkSubprocessPing(strIP):
    # Returns True if host (str) responds to a ping request.
    strParam = '-n' if platform.system().lower() == 'windows' else '-c'
    strCommand = ['ping', strParam, '1', strIP]
    return subprocess.call(strCommand) == 0
