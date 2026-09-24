import time
from colorama import Fore,init

def print_lyric(text,color):
    for char in text:
        print(color+char,end="",flush=True)#end is used to defuse the default \n in the print
        time.sleep(0.11)
    print()#this is to put the new lyrics in the new line

lyrics = [
    ("Tere jhoote alfaaz", Fore.RED, 0.2),
    ("Don't be a dhokebaaz", Fore.YELLOW, 0),
    ("Baatein saari bekaar", Fore.CYAN, 0),
    ("Ja re ja, ja re", Fore.GREEN, 0),
    ("Ye do din ka faaltu pyaar", Fore.MAGENTA, 0),
    ("Ik pal ka bharosa", Fore.BLUE, 0.5),
    ("Karun kyun, meri jaan?", Fore.RED, 0.5),
    ("Ja re ja, ja re ja", Fore.YELLOW, 1)
]

for line, color, delay in lyrics:
    print_lyric(line, color)
    time.sleep(delay)