import requests
import os
from dotenv import load_dotenv

load_dotenv()
webhook = os.environ["WEBHOOK_URL"]

games = {"storeID": 1,"steamAppID":"1593500,2322010,3357650,1984270" }
r = requests.get("https://www.cheapshark.com/api/1.0/deals",params= games)
r = r.json()

hours ={
  "1593500" : 33,
  "2322010" : 41,
  "3357650" : 16,
  "1984270" : 46,

}

def gamesale(game,hours):
    master = " "
    for i in game:
      onSale = i["isOnSale"]
      if onSale == "1":
        id = i["steamAppID"]
        hrs = hours[f"{id}"]
        title = i["title"]
        price = i["salePrice"]
        equation = round(float(price) / hrs,2)
        videogame = f"{title} = {price}  / price / hrs : {equation}\n"
        master += videogame
    print(master)
    requests.post(webhook,json={"content":master})
      

gamesale(r,hours)