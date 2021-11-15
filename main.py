from colorama import Fore
from kahoot import client
import pyfiglet
import random
import sys

def joinHandle():
  pass

print(Fore.BLUE + pyfiglet.figlet_format("Kahoot Bot"))
print(Fore.BLUE + "Coded by AsyncCode <3 | ")
username = input(Fore.BLUE + "Tell me the Bots name. > ")
code = input(Fore.BLUE + "Tell me the Kahoot's Game Code. > ")
int(code)
if code.isdigit() is False:
  print(Fore.BLUE + "Error, the Code must be an Integer.")
  sys.exit(1)
logging = input(Fore.BLUE + "Tell me if you want to enable logging. y / n > ")

while 0 < 1:
  bot = client()
  BotID = random.randint(1000000, 10000000)
  BotID = str(BotID)
  bot.join(code, username + " - " + BotID)
  bot.on("joined",joinHandle)
  if logging == "y":
    print(Fore.BLUE + "Log: Joining the Game (" + code + ") with Name: " + username + " - " + BotID + ".")
  BotID = int(BotID)