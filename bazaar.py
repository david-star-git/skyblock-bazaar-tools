import requests
import json
from datetime import datetime
import re
import math
from colorama import Fore, Back, Style

###--- API ---###
def getInfo():
    r = requests.get("https://api.hypixel.net/skyblock/bazaar")
    return r.json()
#bazaar = getInfo()

###--- getInformation ---###
def info():
    wanted = input("input: ").upper()
    wanted = wanted.replace(" ", "_" )
    if "true" == "true":
        for i in bazaar["products"]:
            if wanted in i:
                name = (bazaar["products"][i]["quick_status"]["productId"])
                # Getting the price
                try:
                    buyPrice = (bazaar["products"][i]["sell_summary"][0]["pricePerUnit"])
                except:
                    buyPrice = "None"
                
                try:
                    sellPrice = (bazaar["products"][i]["buy_summary"][0]["pricePerUnit"])
                except:
                    sellPrice = "None"
                
                try:
                    rated = (bazaar["products"][i]["quick_status"]["sellMovingWeek"])/100000
                except:
                    rated = 0
                # Check if price is positive
                if sellPrice != "None":
                    if buyPrice != "None":
                        margin = ((sellPrice - buyPrice))
                        margin = (margin - (margin*.0125)) # 1.25% tax
                    else:
                        margin = "None"
                else:
                    margin = "None"

                # Formating the numbers
                prof = margin
                try:
                    sellPrice = str(("{:,}".format(sellPrice)).split('.')[0])
                    buyPrice = str(("{:,}".format(buyPrice)).split('.')[0])
                    margin = str(("{:,}".format(margin)).split('.')[0])
                    rated = str(("{:,}".format(rated)).split('.')[0])
                except:
                    pass
                
                try:
                    if prof > 0:
                        print(Fore.BLUE + name + Fore.CYAN + '     buyPrice ' + buyPrice + Fore.MAGENTA + '     sellPrice ' + sellPrice + Fore.YELLOW + '     raring ' + rated + Fore.GREEN + '     profit ' +Fore.GREEN + margin + Style.RESET_ALL)
                except:
                    pass

                try:
                    if prof < 0:
                        print(Fore.BLUE + name + Fore.CYAN + '     buyPrice ' + buyPrice + Fore.MAGENTA + '     sellPrice ' + sellPrice + Fore.YELLOW + '     raring ' + rated + Fore.RED + '     profit ' +Fore.RED + margin + Style.RESET_ALL)
                except:
                    pass

                try:
                    if prof == "None":
                        print(Fore.BLUE + name + Fore.CYAN + '     buyPrice ' + buyPrice + Fore.MAGENTA + '     sellPrice ' + sellPrice + Fore.YELLOW + '     raring ' + rated + Fore.RED + '     profit ' +Fore.RED + margin + Style.RESET_ALL)
                    print('')
                except:
                    pass
while True:
    bazaar = getInfo()
    info()
    print('')
    print('')
