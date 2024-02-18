# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:22:51 2024

@author: CyberMan
"""

import socket

print("""
      
      [+]  ابزار جمع اوری اطلاعات مدیر وب سایت



  _____            _                      _   _             _    _                          _   _____                 _          _     _            _ 
 |  __ \          (_)                    | | | |           | |  | |                        | | |  __ \               | |        (_)   | |          (_)
 | |  | | ___  ___ _  __ _ _ __   ___  __| | | |__  _   _  | |__| | __ _ _ __ ___   ___  __| | | |__) |__  _   _ _ __| |__   ___ _  __| | __ _ _ __ _ 
 | |  | |/ _ \/ __| |/ _` | '_ \ / _ \/ _` | | '_ \| | | | |  __  |/ _` | '_ ` _ \ / _ \/ _` | |  ___/ _ \| | | | '__| '_ \ / _ \ |/ _` |/ _` | '__| |
 | |__| |  __/\__ \ | (_| | | | |  __/ (_| | | |_) | |_| | | |  | | (_| | | | | | |  __/ (_| | | |  | (_) | |_| | |  | | | |  __/ | (_| | (_| | |  | |
 |_____/ \___||___/_|\__, |_| |_|\___|\__,_| |_.__/ \__, | |_|  |_|\__,_|_| |_| |_|\___|\__,_| |_|   \___/ \__,_|_|  |_| |_|\___|_|\__,_|\__,_|_|  |_|
                      __/ |                          __/ |                                                                                            
                     |___/                          |___/                                                                                             


 
                 [+] نسخه 1.2


      """)

print("لطفا بدون پیشوند http  و https  باشد")
print("""
      
      """)

domain = input("نام سایت خود را وارد نمایید ===> ").lower()

print("""
      

  ___           ___ 
 |  _|    _    |_  |
 | |    _| |_    | |
 | |   |_   _|   | |
 | |     |_|     | |
 | |_           _| |
 |___|         |___|
                    


      """)

domain = domain.replace("http://","")
domain = domain.replace("https://","")
domain = domain.replace("www.","")

if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
    whois_server = "whois.internic.net"
else:
    whois_server =  "whois.iana.org"

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

s.connect((whois_server,43))

s.send((domain+"\r\n").encode())

msg = s.recv(10000)

print(msg.decode())