import requests
from bs4 import BeautifulSoup
import requests
import pandas as pd
import requests
import datetime
import numpy as np
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# SPOTIFY API CONNECT & USER LOGIN
SPOTIFY_CLIENT_ID = "d4c88e10069d4bf789bf0d70cb71114a"
SPOTIFY_CLIENT_SECRET = "51dee21966eb485eae0ee1320f731dba"
SCOPE = "user-top-read"
REDIRECT_URI = "http://localhost:8888/callback/"
# user log in – won't work from .ipynb, download as .py and run
# token = util.prompt_for_user_token(scope=SCOPE,client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI)

def getConcertData(eventId):
    apikey = '0oiXuNOurAs4uGkbcByIC8bWWRZ8DhbN'
    url = 'https://app.ticketmaster.com/discovery/v2/events/{}?apikey={}'.format(eventId, apikey)
    jsonresponse = requests.get(url).json()

    show = {}

    if not '_embedded' in jsonresponse:
        return show
    
    img         = jsonresponse['images'][0]['url']
    name        = jsonresponse['name']
    date        = jsonresponse['dates']['start']['localDate']
    # time        = jsonresponse['dates']['start']['time']
    genre       = jsonresponse['classifications'][0]['genre']['name']
    priceMin    = jsonresponse['priceRanges'][0]['min']
    priceMax    = jsonresponse['priceRanges'][0]['max']
    venue       = jsonresponse['_embedded']['venues'][0]['name']
    city        = jsonresponse['_embedded']['venues'][0]['city']['name']
    country     = jsonresponse['_embedded']['venues'][0]['country']['name']

    show.update({'img': img})
    show.update({'name': name})
    show.update({'date': date})
    # show.update({'time': time})
    show.update({'genre': genre})
    show.update({'priceMin': priceMin})
    show.update({'priceMax': priceMax})
    show.update({'venue': venue})
    show.update({'city': city})
    show.update({'country': country})

    return show

def getConcerts(artist):
    link = 'https://app.ticketmaster.com/discovery/v2/events.json?size=20&keyword=' + artist + '&sort=relevance,desc&apikey=sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'
    jsonresponse = requests.get(link).json()
    events = []

    for i in range(0, len(jsonresponse['_embedded']['events'])):
        print(i)
        event   = jsonresponse['_embedded']['events'][i]
        show    = getConcertData(event['id'])
        if (not "name" in show):
            continue
        events.append(show)    
    return events