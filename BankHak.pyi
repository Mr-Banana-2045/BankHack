from random import choice
import time
import requests
class color:
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	cyan = '\033[96m'
	blue = '\033[94m'
	white = '\033[97m'
print(f"""{color.cyan}
__________                __     ___ ___         __
\______   \_____    ____ |  | __/   |   \_____  |  | __ {color.yellow}| {color.blue}Tools name > BankHak{color.cyan}
 |    |  _/\__  \  /    \|  |/ /    ~    \__  \ |  |/ / {color.yellow}| {color.blue}Tools options > Get cvv2 Get password{color.cyan}
 |    |   \ / __ \|   |  \    <\    Y    // __ \|    < {color.yellow} | {color.red}-------------------{color.cyan}
 |______  /(____  /___|  /__|_ \\___|_  /(____  /__|_ \  {color.blue}github > https://github.com/Mr-Banana-2045{color.cyan}
        \/      \/     \/     \/      \/      \/    \/  {color.blue}channel > God developers{color.cyan}
        
{color.yellow}  ⟬ 1 ⟭ ⟞ {color.green}Receive bank card information
 {color.yellow} ⟬ 2 ⟭ ⟞ {color.green}get cvv2-password
""")
moz = float(input(f"{color.cyan}enter number > {color.white}"))
if moz >= 1:
	if moz == 2:
		lolo = input(f"{color.cyan}[ pass-cvv2 ] enter terget Bank card number > {color.white}")
		for i in range(20):
			time.sleep(2)
			print(f"{color.yellow}[-] {color.red}error of cvv2 no sorry number card : {lolo} > ?")
		x , lis = open("cvv2_pass.txt","r").read().split("\n") , []
		for item in x:
			lis.append(item)
		sho = (choice(lis))
		print(f"{color.yellow}[+]{color.green} cvv2 user number target : {lolo} > "+sho)
		for i in range(25):
			time.sleep(1.5)
			print(f"{color.yellow}[-] {color.red}error of pssword no sorry number card : {lolo} > ?")
		m , liis = open("cvv2_pass.txt","r").read().split("\n") , []
		for item in m:
			liis.append(item)
		shoo = (choice(liis))
		print(f"{color.yellow}[+]{color.green} password user number target : {lolo} > "+shoo)
	else:
		hosh = input(f"{color.cyan}enter number card bank target > {color.white}")
		goz1 = requests.get(f"https://randomuser.me/api?{hosh}")
		jok = (goz1.text)
		with open("Target_information.txt", 'w') as f:
			f.write(jok)
			f.close()
			print(f"{color.yellow}[+]{color.green} The file was saved in the device memory")