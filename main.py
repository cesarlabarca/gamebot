import requests
import os
from dotenv import load_dotenv

load_dotenv()
webhook = os.environ["WEBHOOK_URL"]

games = {"storeID": 1,"steamAppID":"1593500,2322010,3357650,1984270" }
r = requests.get("https://www.cheapshark.com/api/1.0/deals",params= games)
r = r.json()


def gamesale(game):
    master = " "
    for i in game:
      onSale = i["isOnSale"]
      if onSale == "1":
        title = i["title"]
        price = i["salePrice"]
        videogame = f"{title} = {price} \n"
        master += videogame
    print(master)
    requests.post(webhook,json={"content":master})
      

gamesale(r)