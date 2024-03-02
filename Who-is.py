from ipwhois import IPWhois
from pprint import pprint
import whois,socket
import time

time.sleep(1)

print("""
__        ___           _                                            
\ \      / / |__   ___ (_)___                                
 \ \ /\ / /| '_ \ / _ \| / __|                                
  \ V  V / | | | | (_) | \__ \                                   
   \_/\_/  |_| |_|\___/|_|___/                                     
      
        | Developed by Gifted-Tech
        | Telegram @giftedtechnexus
        | Version 2.0.1
""")

site = input("Enter Target Domain : ")

time.sleep(2)

ip = socket.gethostbyname(site)

print(f"""
---------------------
[+] Target IP : {ip}
---------------------
""")

info = IPWhois(ip)

info = info.lookup_whois()
print("""
---------------------
[+] Server Information : 
---------------------
""")
pprint(info)

print("========================================================")

res = whois.whois(site)
print("""
---------------------
[+] Domain Information : 
---------------------
""")
pprint(res)
