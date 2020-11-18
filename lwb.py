import os
import sys
import time 
import pyfiglet
from datetime import datetime as dt 

print (chr(27)+"[33m")

os.system("clear")

banner = pyfiglet.figlet_format("Website Blocker",font="big")
print(banner)

print (chr(27)+"[35m"+"               Author : Rahat Khan Tusar(RKT)")
print (chr(27)+"[35m"+"               Github : https://github.com/r3k4t")

# change hosts path according to your OS 
hosts_path = "/etc/hosts"
# localhost's IP 
redirect = "127.0.0.1"
  
# websites That you want to block
 
rkt = open("weblist.txt","r+")

print (chr(27)+"[31m")
 
while True: 
  
    # time of your work 
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
        print("Site Blocked ...") 
        with open(hosts_path, 'r+') as file: 
            content = file.read() 
            for website in rkt: 
                if website in content: 
                    pass
                else: 
                    # mapping hostnames to your localhost IP address 
                    file.write(redirect + " " + website + "\n") 
    else: 
        with open(hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in rkt): 
                    file.write(line) 
                    
  
            # removing hostnmes from host file 
            file.truncate() 
  
        print("FUN TIME...") 
    time.sleep(2)
    
