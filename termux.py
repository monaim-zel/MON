import os
os.system('pip2 install V7xStyle')
from V7xStyle import *
import time
import sys
#############################
os.system('clear')
an=Animation
def menu():

    s=Style("""###############################################
#G#name my channel: Y#Monaim android        W#      #
#G#my number whatsapp:Y#+212650056998      W#       #
###############################################
#Y#1-) G#install command linux            W#         #
###############################################
#Y#00-)G#Exit the tool                   W#         #
###############################################""").Square(cols=2,Equal=True)
    print(s)

loop = True

while loop:
    menu()
    what = input("\033[1;32mMon#: ")
    
    if what == "1":
        to10=[str(i+1)+'% ' for i in range(100)]
        an.Loading(AT=to10,text='R#Wait Please..Y#',repeat=1,t=0.02)
        print("===================================")
        print("----------------")
        hm = input("presse y to continue (y/n): ")
        print("================================")
        if hm == "y":
            an.Loading(text='Y#Loading.... R#')
            print("========================================================")
            print("[+] Please put down you android and go to the toilet...")
            print("Because this will take a long time.")
            print("========================================================") 
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt-get install python -y")
            os.system("apt-get install python2 -y")
            os.system("apt-get install python3 -y")
            os.system("apt-get install ruby -y")
            os.system("apt-get install git -y     ")
            os.system("apt-get install php -y")
            os.system("apt-get install nano -y")
            os.system("apt-get install nmap -y")
            os.system("apt-get install perl -y")
            os.system("termux-setup-storage -y")
            os.system("apt-get install golang -y")
            os.system("apt-get install host -y")
            os.system("apt-get install havij -y")
            os.system("apt-get install hydra -y")
            os.system("apt install wireshark -y")
            os.system("apt-get install cmatrix -y")
            os.system("apr-get install figlet -y")
            os.system("apt-get install wget -y")
            os.system("apt-get install wget -y")
            os.system("apt-get install python2-dev -y")
            os.system("apt install wireshark -y")
            os.system("apt-get install cowsay -y")
            os.system("apt-get install toilet -y")
            os.system("apt-get install curlinstall wgetrc -y")
            os.system("apt-get install ruby -y")
            os.system("apt-get install help -y")
            os.system("apt-get install net-tools -y")
            os.system("apt-get install w3m -y")
            os.system("apt-get install unrar -y ")
            os.system("apt-get install clang -y")
            os.system("apt-get install openssh -y")
            os.system("apt-get install openssl -y")
            os.system("apt-get install tor -y")
            os.system("apt-get install tar -y")
            os.system("apt-get install zip -y")
            os.system("apt-get install proot -y")
            os.system("pip2 install wget -y")
            os.system("pip2 install requests -y")
            os.system("gem install lolcat -y")
            os.system("apt update -y && apt upgrade -y")
            os.system("clear")            
            print("====================================")
            print("[+] routersploit installed successfully :)")
            print("[+] Go to routersploit folder and type 'python2 rsf.py' to start.")
            print("====================================")
            rmenu = input("[?] Back to Menu? (y/n): ")
            if rmenu == "y":
                os.system('clear')
                python = sys.executable
                os.execl(python,python, * sys.argv)
            else:
                break
    elif what == "00":
        print("Bye...!")
        break
