import platform
from colorama import Fore,Back,Style
import os
check=234
envir=platform.system()
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

def corrupt(f_name):
    global state
    try:
        file=open(f_name,'rb')
    except FileNotFoundError:
        state='File not found!'
        return
    content=file.read().hex()
    file.close()
    s_val='49484452'
    r_val='ff484452'
    print(s_val in content)
    if s_val in content:
        content=content.replace(s_val,r_val)
        file=open(f_name,'wb')
        file.write(bytes.fromhex(content))
        file.close()
        state='File Corrupted...successfully'
        print("File Corrupted...successfully")
    else:
        state='Error or invalid operation'

def recov(f_name):
    global state
    try:
        file=open(f_name,'rb')
    except FileNotFoundError:
        state='File not found!'
        return
    content=file.read().hex()
    file.close()
    r_val='49484452'
    s_val='ff484452'
    print(s_val in content)
    if s_val in content:
        content=content.replace(s_val,r_val)
        file=open(f_name,'wb')
        file.write(bytes.fromhex(content))
        file.close()
        state='File Recovered...successfully'
        print("File Recovered...successfully")
    else:
        state='Error or invalid operation'

def disp_banner():
    print(f'''{Style.BRIGHT}-------------------------
|{Fore.RED}{Back.GREEN}{Style.BRIGHT}***********************{Fore.WHITE}{Style.RESET_ALL}|
{Style.BRIGHT}-------------------------
          |{Fore.RED}{Style.BRIGHT}*{Fore.WHITE}|   {Fore.RED}|{Fore.BLUE}|{Style.RESET_ALL}      |
          |{Fore.RED}{Style.BRIGHT}*{Fore.WHITE}|   {Fore.RED}|{Fore.BLUE}|{Style.RESET_ALL}      |
          |{Fore.RED}{Style.BRIGHT}*{Fore.WHITE}|   {Fore.RED}|{Fore.BLUE}|{Style.RESET_ALL}{Back.GREEN}{Style.DIM}------{Style.RESET_ALL}|   --------- 
          |{Fore.RED}{Style.BRIGHT}*{Fore.WHITE}|   {Fore.RED}|{Fore.BLUE}|{Style.RESET_ALL}      |       |     ------ ------ |     | / -------  |
          |{Fore.RED}{Style.BRIGHT}*{Fore.WHITE}|   {Fore.RED}|{Fore.BLUE}|{Style.RESET_ALL}      |       |     |    | |    | |     |/     |    ---
-------------------------       |     |    | |    | |     |\\     |     |
|{Fore.RED}{Back.GREEN}{Style.BRIGHT}***********************{Fore.WHITE}{Style.RESET_ALL}|       |     ------ ------ ----- | \\ -------  ---
{Style.BRIGHT}-------------------------{Style.RESET_ALL}''')
    print(f"{Style.BRIGHT}{Fore.BLUE}======================================================================================")
    print(f"{Style.BRIGHT}{Fore.RED}[{Fore.BLUE}*{Fore.RED}]Note: Check whether this program and the image are at the same folder.")
    print('\n')

def action():
    global imag_name, state
    print(f"{Style.BRIGHT}{Fore.BLUE}======================================================================================")
    print(f"{Fore.RED}{Style.BRIGHT}Action Prompt..\t\t\t\tStatus: {Fore.GREEN}{state}")
    print(f"{Style.BRIGHT}{Fore.BLUE}======================================================================================\n")
    print(f"{Fore.RED}1{Fore.WHITE}){Fore.BLUE} Corrupt PNG")
    print(f"{Fore.RED}2{Fore.WHITE}){Fore.BLUE} Recover PNG")
    if state != 'Initialized..':
        print(f"{Fore.RED}3{Fore.WHITE}){Fore.BLUE} Insert another Image")
    print(f"{Fore.RED}99{Fore.WHITE}){Fore.BLUE} Exit toolkit\n")
    try:
        choice=int(input(f"{Fore.GREEN}Enter the Action value (must be integer):{Fore.BLUE} "))
    except:
        state="Invalid Input!"
        return True
        
    match choice:
        case 1:
            corrupt(imag_name)
        case 2:
            recov(imag_name)
        case 3:
            if state != 'Initialized..':
                imag_name=input(f"{Fore.GREEN}Enter the file name with extension ({Fore.RED}*Use '{Fore.BLUE}ls' or 'dir{Fore.RED}' to list files*{Fore.GREEN}):{Fore.BLUE} ")    
                while imag_name=='ls' or imag_name=='dir':
                    if True:
                        if envir=='Windows':
                            print(os.system("dir"))
                        else:
                            print(os.system("ls"))
                        imag_name=input(f"{Fore.GREEN}Enter the file name with extension ({Fore.RED}*Use '{Fore.BLUE}ls' or 'dir{Fore.RED}' to list files*{Fore.GREEN}):{Fore.BLUE} ") 
                    else:
                        pass
            else:
                pass
        case 99:
            if envir=='Windows':
                os.system('cls')
            else:
                os.system('clear')
            exit()
        case _:
            pass
     

state='Initialized..'
if envir=='Windows':
    os.system('cls')
else:
    os.system('clear')
disp_banner()
imag_name=input(f"{Fore.GREEN}Enter the file name with extension ({Fore.RED}*Use '{Fore.BLUE}ls' or 'dir{Fore.RED}' to list files*{Fore.GREEN}):{Fore.BLUE} ")    
while imag_name=='ls' or imag_name=='dir':
    if True:
        if envir=='Windows':
            print(os.system("dir"))
        else:
            print(os.system("ls"))
        imag_name=input(f"{Fore.GREEN}Enter the file name with extension ({Fore.RED}*Use '{Fore.BLUE}ls' or 'dir{Fore.RED}' to list files*{Fore.GREEN}):{Fore.BLUE} ") 
    else:
        pass

while check!=0:
    if envir=='Windows':
        os.system('cls')
    else:
        os.system('clear')
    disp_banner()
    action()
