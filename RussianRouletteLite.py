# ╔═══════════════════════════════════►
# ║   Made by sava4ka.
# ║   12/8/2021
# ║   Time spent: 30 minutes
# ║   It's my second time using Python.
# ║   If you use it somewhere, credit the author. (But why would you do that, thats such a shit)
# ║
# ║
# ║  Github: https://github.com/sava4ka777/RRoulette
# ║
# ║  Luv u :3
# ║  ║▌│█│║▌║█║│║▌║
# ║  ║▌│█│║▌║█║│║▌║
# ║  ║▌│█│║▌║█║│║▌║
# ╚═══════════════════════════════════►
#Modules
import os
import random
from colorama import init
init()
from colorama import Fore, Back, Style
import time

#Logo
print(Fore.RED + "██████╗░██████╗░░█████╗░██╗░░░██╗██╗░░░░░███████╗████████╗████████╗███████╗")
print(Fore.RED + "██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░░░██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝")
print(Fore.RED + "██████╔╝██████╔╝██║░░██║██║░░░██║██║░░░░░█████╗░░░░░██║░░░░░░██║░░░█████╗░░")
print(Fore.RED + "██╔══██╗██╔══██╗██║░░██║██║░░░██║██║░░░░░██╔══╝░░░░░██║░░░░░░██║░░░██╔══╝░░")
print(Fore.RED + "██║░░██║██║░░██║╚█████╔╝╚██████╔╝███████╗███████╗░░░██║░░░░░░██║░░░███████╗")
print(Fore.RED + "╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝")
print(Fore.RED + "                                                     made by sava4ka       ")

#Line skip
print("")

#Rules
print(Fore.YELLOW + "It's like a russian roulette, but if you loose your pc restarts.")
#Line skip
print("")
#Continue
input(Fore.WHITE + "Press enter to continue.")
#Countdown
time.sleep(1)
print(Fore.GREEN + "3")
time.sleep(1)
print(Fore.YELLOW + "2")
time.sleep(1)
print(Fore.RED + "1")
time.sleep(1)
#Number generation
random_number = random.randint(1,5)
#Shot or not
if random_number == 5:
 print (Fore.RED + "Oh no, bad luck!")
 time.sleep(2)
 os.system("shutdown /s /t 1")
if random_number != 5:
 print(Fore.YELLOW + "*click*")
 time.sleep(1)
 print(Fore.GREEN + "You good")
