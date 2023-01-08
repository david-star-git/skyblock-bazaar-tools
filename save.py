import requests
import json
from datetime import datetime
import re
import math
import os

###--- API ---###
def getInfo():
    r = requests.get("https://api.hypixel.net/skyblock/bazaar")
    return r.json()
bazaar = getInfo()

###--- saving information ---###
date = datetime.now()
date_time = date.strftime("%d-%m-%Y")

if (os.path.exists(f'{date_time}.json') == False):
    f = open(f'{date_time}.json', 'a')
    f.write('[\n{')
    f.write('"Template":[\n{\n"sellPrice": 0,\n"buyPrice": 0,\n"rating": 0,\n"margin": 0\n}]')
else:
    print('File Exists')

count = 0


for i in bazaar["products"]:
    name = (bazaar["products"][i]["quick_status"]["productId"])
    name = name.replace(":", "" )
    # Getting the price
    try:
        buyPrice = (bazaar["products"][i]["sell_summary"][0]["pricePerUnit"])
    except:
        buyPrice = 0
    
    try:
        sellPrice = (bazaar["products"][i]["buy_summary"][0]["pricePerUnit"])
    except:
        sellPrice = 0

    try:
        rated = (bazaar["products"][i]["quick_status"]["sellMovingWeek"])/100000
    except:
        rated = 0
    # Check if price is positive
    if sellPrice != 0:
        if buyPrice != 0:
            margin = ((sellPrice - buyPrice))
            margin = (margin - (margin*.0125)) # 1.25% tax
        else:
            margin = 0
    else:
        margin = 0

    # Formating the numbers
    prof = margin
    try:
        sellPrice = str(("{:}".format(sellPrice)).split('.')[0])
        buyPrice = str(("{:}".format(buyPrice)).split('.')[0])
        margin = str(("{:}".format(margin)).split('.')[0])
        rated = str(("{:}".format(rated)).split('.')[0])
    except:
        pass

    f.write(',\n\n"'+name+'":['+'\n{\n"sellPrice": '+sellPrice+',\n"buyPrice": '+buyPrice+',\n"rating": '+rated+',\n"margin": '+margin+'\n}]')
    count += 1

f.write('}\n]')
f.close()
print(count)