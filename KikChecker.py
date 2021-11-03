#made with love, by synth#
import os, time, requests
from threading import Thread
from colorama import init, Fore
init()

os.system("title Kik Name Checker || by synth")
cwd = os.path.dirname(os.path.realpath(__file__))
names = open(f"{cwd}\\usernames.txt", 'r').read().splitlines()

def logo():
    os.system('cls;clear')
    print("""
 /$$   /$$ /$$ /$$                                                    
| $$  /$$/|__/| $$                                                    
| $$ /$$/  /$$| $$   /$$                                              
| $$$$$/  | $$| $$  /$$/                                              
| $$  $$  | $$| $$$$$$/                                               
| $$\  $$ | $$| $$_  $$                                               
| $$ \  $$| $$| $$ \  $$                                              
|__/  \__/|__/|__/  \__/                                                                                                                                                                               
                                                                      
  /$$$$$$  /$$                           /$$                          
 /$$__  $$| $$                          | $$                          
| $$  \__/| $$$$$$$   /$$$$$$   /$$$$$$$| $$   /$$  /$$$$$$   /$$$$$$ 
| $$      | $$__  $$ /$$__  $$ /$$_____/| $$  /$$/ /$$__  $$ /$$__  $$
| $$      | $$  \ $$| $$$$$$$$| $$      | $$$$$$/ | $$$$$$$$| $$  \__/
| $$    $$| $$  | $$| $$_____/| $$      | $$_  $$ | $$_____/| $$      
|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$| $$      
 \______/ |__/  |__/ \_______/ \_______/|__/  \__/ \_______/|__/      
                                                                                                                                    
   Created with ♥ by synth#7222 || https://github.com/edgyandcoolname
   """.replace('█', Fore.WHITE + '█' + Fore.LIGHTMAGENTA_EX))

logo()

def check_name(name):
    r = requests.get(f"https://ws2.kik.com/user/{name}")
    if r.status_code == 404:
        print(f"{Fore.GREEN}[{Fore.LIGHTGREEN_EX}AVAILABLE{Fore.GREEN}]{Fore.WHITE} {name}")
        with open('available.txt', 'a') as (f):
            f.write(name + '\n')
    else:
        print(f"{Fore.RED}[{Fore.LIGHTRED_EX}UNAVAILABLE{Fore.RED}]{Fore.WHITE} {name}")


threads = []
for name in names:
    threads.append(Thread(target=check_name, args=[name]))

for t in threads:
    t.start()
    time.sleep(1)

for t in threads:
    t.join()

    
