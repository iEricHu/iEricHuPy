import subprocess

cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)