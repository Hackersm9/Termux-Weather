import os,sys

os.system("clear")
print(
'''
\033[0;33m░██╗░░░░░░░██╗███████╗░█████╗░████████╗██╗░░██╗███████╗██████╗░  ░░░░░░
░██║░░██╗░░██║██╔════╝██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗  ░░░░░░
░╚██╗████╗██╔╝█████╗░░███████║░░░██║░░░███████║█████╗░░██████╔╝  █████╗
░░████╔═████║░██╔══╝░░██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗  ╚════╝
░░╚██╔╝░╚██╔╝░███████╗██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║  ░░░░░░
░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░░░░░░\033[0m

\033[0;31m███████╗░█████╗░██████╗░███████╗░█████╗░░█████╗░░██████╗████████╗
██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
█████╗░░██║░░██║██████╔╝█████╗░░██║░░╚═╝███████║╚█████╗░░░░██║░░░
██╔══╝░░██║░░██║██╔══██╗██╔══╝░░██║░░██╗██╔══██║░╚═══██╗░░░██║░░░
██║░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░░██║██████╔╝░░░██║░░░
╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░\033[0m
''')
cast = int(input("\033[1;36mEnter your Choice: \033[0m"))
if (cast == 1):
    os.system("python3 weather.py")
if (cast == 2):
     os.system("python3 weather2.py")
if (cast == 3):
	print("\033[1;31mOption 3 is not Available Yet\033[0m")
else:
    print("Done !")