from colorama import Fore, Back, Style, init

init(autoreset=True)
t = "FROM UKRAINE"

ct = f"{Fore.BLUE}{t[:4]} {Fore.YELLOW}{t[5:]}"

print(ct)
