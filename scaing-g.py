import requests
import json
import socket
import os
import json
import codecs
import sys
import readline
import time
import ftplib
from colorama import Fore
import urllib.request as urllib2
print(f"{Fore.RED}[+] {Fore.WHITE}Check orders ........")
print(f"{Fore.RED}[+] {Fore.WHITE}done check")
time.sleep(1.0)
os.system('clear')
#color
w = Fore.WHITE
r = Fore.CYAN
c = Fore.LIGHTBLUE_EX
rr = Fore.LIGHTRED_EX
banner = Fore.BLUE+"""
        ███████╗ ██████╗ █████╗ ███╗   ██╗       ██████╗ 
        ██╔════╝██╔════╝██╔══██╗████╗  ██║      ██╔════╝ 
        ███████╗██║     ███████║██╔██╗ ██║█████╗██║  ███╗
        ╚════██║██║     ██╔══██║██║╚██╗██║╚════╝██║   ██║
        ███████║╚██████╗██║  ██║██║ ╚████║      ╚██████╔╝
        ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝       ╚═════╝ 
"""
print(banner)
while True:
    cmd = input(f"{r}scaning> {w}")

#command help
    if cmd.split()[0] =='help':
        print(f"{Fore.WHITE}Misc:")
        print(f"   {Fore.BLUE}whoami : {Fore.RED}who am i..!")
        print(f"   {Fore.BLUE}clear : {Fore.RED}It cleans the terminal")
        print(f"   {Fore.BLUE}team : {Fore.RED}People who helped me")
        print(f"   {Fore.BLUE}exit : {Fore.RED}Get you out of the tool")
        print(f"   {Fore.BLUE}myip : {Fore.RED}It tells you what the ip is and the name of your device")
        print(f"   {Fore.BLUE}banner : {Fore.RED}print my banner.. :)")
        print(f"{Fore.WHITE}Tools:")
        print(f"   {Fore.BLUE}links : {Fore.RED}Searches for website paths")
        print(f"   {Fore.BLUE}headers : {Fore.RED}It pulls headers from the site")
        print(f"   {Fore.BLUE}findshareddns : {Fore.RED}Determine the hosts and the websites associated with the systems")
        print(f"   {Fore.BLUE}mtr : {Fore.RED}Identifies IP Addresses - Network Path")
        print(f"   {Fore.BLUE}portscan : {Fore.RED}It checks the open ports")
        print(f"   {Fore.BLUE}macinfo : {Fore.RED}Extracting the largest amount of information from the mac address")
        print(f"   {Fore.BLUE}checkurl : {Fore.RED}Tracks guess the location of a file")
        print(f"   {Fore.BLUE}checkprox : {Fore.RED}Check the ip address online or ofline")
        print(f"   {Fore.BLUE}checkmac : {Fore.RED}Check the mac address online or ofline")

    if cmd.split()[0] =='banner':
        print(banner)
    #MTR
    if cmd.split()[0] =='mtr':
        try:
            cmd_mtr = cmd.split()[1]
            requests_cmd = requests.get(f'https://api.hackertarget.com/dnslookup/?q={cmd_mtr}').text
            print(Fore.BLUE+requests_cmd)
        except:
            print(f"{r}[{rr}-{r}] mtr < {c}url{c} >")
            print(f"{r}[{rr}-{r}] mtr < {c}google.com{c} >")
    
    #headers
    if cmd.split()[0] =='headers':
        try:
            cmd_headers = cmd.split()[1]
            requests_headers = requests.get(f'https://api.hackertarget.com/httpheaders/?q={cmd_headers}').text
            print(Fore.BLUE+requests_headers)
        except:
            print(f"{Fore.BLUE}[{Fore.RED}-{BLUE}]headers < {Fore.CYAN}url{Fore.BLUE} >")
            print(f"{Fore.BLUE}[{Fore.RED}-{BLUE}]headers < {Fore.CYAN}google.com{Fore.BLUE} >")
    
    #links
    if cmd.split()[0] =='links':
        cmd_link = cmd.split()[1]
        requests_link = requests.get(f'https://api.hackertarget.com/pagelinks/?q={cmd_link}').text
        print(Fore.CYAN+requests_link)
    
    #port scan
    try:
        if cmd.split()[0] =='portscan':
            cmd_scan = cmd.split()[1]
            requests_nmap = requests.get(f'https://api.hackertarget.com/nmap/?q={cmd_scan}').text
            print(requests_nmap)
    except:
        print("portscan < ip >")
        print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}]portscan < {Fore.CYAN}8.8.8.8{Fore.BLUE} >")

    #find dns
    if cmd.split()[0] =='finddns':
        try:
            cmd_find = cmd.split()[1]
            requsests_find = requests.get(f'https://api.hackertarget.com/findshareddns/?q={cmd_find}').text
            print(requsests_find)
        except:
            print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}] finddns < url >")
            print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}] finddns < {Fore.CYAN}google.com {Fore.BLUE}>")

    #my ip
    if cmd.split()[0] =='myip':
        hostname = socket.gethostname()   
        IPAddr = socket.gethostbyname(hostname)   
        print(f"[{Fore.BLUE}+{w}] Your Computer Name is:" + hostname)   
        print(f"[{Fore.BLUE}+{w}] Your Computer IP Address is:" + IPAddr)
    #who am i
    if cmd.split()[0] =='whoami':
        print(f"{Fore.LIGHTBLUE_EX}@ {w}tsy7")
    
    #my team
    if cmd.split()[0] =='team':
        print(f"{Fore.RED}@ {Fore.BLUE}tsy7")
        print(f"{Fore.RED}@ {Fore.BLUE}spooky_sec")
        print(f"{Fore.RED}@ {Fore.BLUE}t8qu_")
        print(f"{Fore.RED}@ {Fore.BLUE}d5tr")
        print(f"{Fore.RED}@ {Fore.BLUE}hereioz")

    #exit
    if cmd.split()[0] =='exit':
        print(f"{Fore.BLUE}Good Bye....!")
        break

    #clear
    if cmd.split()[0] =='clear':
        os.system('clear')
    if cmd.split()[0] =='CLEAR':
        os.system('clear')
    
    #url check
    if cmd.split()[0] =='checkurl':
        try:
            cmd_url = cmd.split()[1]
            cmd_file = cmd.split()[2]
            file = open(cmd_file, 'r').readlines()
            for file in file:
                x = file.strip()
                req = requests.get(cmd_url+x).status_code
                if req == 404:
                    pass
                if req == 200:
                    print(f"[{Fore.BLUE}+{Fore.WHITE}] {cmd_url}{x} : {Fore.BLUE}{req}{Fore.WHITE}")
        except:
            print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}] check url < {Fore.CYAN}file.txt{Fore.BLUE} >")

    #guess ftp
    if cmd.split()[0] =='ftpcrack':
        try:
            ip_cmd = cmd.split()[1]
            usertarget_cmd = cmd.split()[2]
            file_cmd = cmd.split()[3]
            filex = open(file_cmd, 'r').readlines()
            for ii in filex:
                xx = ii.strip()
        except:
            print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}] ftpcrack < ip > < user > < file.txt >")
            try:
                ftb_login = ftplib.FTP(ip_cmd,usertarget_cmd,xx)
                print(f"[{Fore.GREEN}+{Fore.WHITE}] done:", ip_cmd,usertarget_cmd,xx)
            except:
                print(f"[{Fore.RED}-{Fore.WHITE}]bad:", ip_cmd,usertarget_cmd,xx)
    if cmd.split()[0] =='macinfo':
        try:
            url = "http://macvendors.co/api/"
            cmd_mac = cmd.split()[1]
            mac_address = cmd_mac

            request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
            response = urllib2.urlopen( request )
            reader = codecs.getreader("utf-8")
            obj = json.load(reader(response))
            print("company:", obj['result']['company'])
            print("address:", obj['result']['address'])
            print("start_hex:", obj['result']['start_hex'])
            print("end_hex:", obj['result']['end_hex'])
            print("country:", obj['result']['country'])
            print("type:", obj['result']['type'])
        except:
            print(f"{Fore.BLUE}[{Fore.RED}-{Fore.BLUE}] macinfo < mac target >")
    if cmd.split()[0] =='checkprox':
        cmd_prox = cmd.split()[1]
        fileo = open(cmd_prox).read().splitlines()
        for fileo in fileo:
            reqq = requests.get(f'https://ipinfo.io/{fileo}').status_code
            if reqq == 200:       
                print(f"[{Fore.GREEN}online{Fore.WHITE}] {fileo}")
            elif reqq == 404:
                print(f"[{Fore.RED}offline{Fore.WHITE}] {fileo}")
    if cmd.split()[0] =='checkmac':
        cmd_mac1 = cmd.split()[1]
        file = open(cmd_mac1).read().splitlines()
        for file in file:
                reqop = requests.get(f'https://api.macvendors.com/{file}').status_code
                if reqop == 200:
                    print(f"[{Fore.GREEN}online{Fore.WHITE}] {file}")
                elif reqop == 404:
                    print(f"[{Fore.RED}offline{Fore.WHITE}] {file}")
            
                        