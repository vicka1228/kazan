from bs4 import BeautifulSoup
import requests
import pandas as pd
import requests
import datetime
import urllib
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
# print(token)

city_populations = {'México': 8855000}

# gets top 100 artists by webscraping 
def getTop100Artists():
    url = 'https://kworb.net/spotify/listeners.html'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    top1000artists = [x.text.strip() for x in soup.find('tbody').find_all('a')]
    
    return top1000artists

# locates city and returns population
def getPopulation(city):
    if(city in city_populations):
        return city_populations[city]
    link = 'https://documentation-resources.opendatasoft.com/api/records/1.0/search/?dataset=geonames-all-cities-with-a-population-1000&q=%s&facet=city'
    url = link % urllib.parse.quote(city)
    resp = requests.get(url)
    respjson = resp.json()
    if(len(respjson['records']) == 0):
        return -1
    city_population = respjson['records'][0]['fields']['population']
    city_populations[city] = city_population
    return city_population

# gives artist rating
def getPopularity(artist):
    urlartist = artist.replace(" ", "%20")
    header = {"Authorization": "Bearer " + token}
    searchURL = "https://api.spotify.com/v1/search?q={}&type=artist".format(urlartist)
    artist_rating = -1
    try: 
        resp = requests.get(searchURL, headers=header)
        artist_details = resp.json()
        artist_rating = artist_details['artists']['items'][0]['popularity']
    except TimeoutError:
        print('TimeoutError')
    
    return artist_rating

# returns data about upcoming concerts for given artist
def getEventsData(artist):
    link = 'https://app.ticketmaster.com/discovery/v2/events.json?size=20&keyword=' + artist + '&sort=relevance,desc&apikey=sPYngrqc3a29GkMAd2SOBDuPm7VdHT9o'
    jsonresponse = requests.get(link).json()
    events = {}

    if jsonresponse.get(u'_embedded')==None:
        return events

    # iterate over length of embedded events
    for i in range(0, len(jsonresponse.get(u'_embedded').get(u'events'))):
        if jsonresponse.get(u'_embedded').get(u'events')[i].get('priceRanges') != None:
            show = {}
            
            # cleaning up the date of the concert
            year, month, day = "", "", ""
            d8 = jsonresponse.get(u'_embedded').get(u'events')[i].get(u'dates').get(u'start').get(u'localDate')            
            for j in range(0, len(d8)):
                if j >= 0 and j <= 3:
                    year += d8[j]
                elif j >= 5 and j <= 6:
                    month += d8[j]
                elif j > 7 and j <= 9:
                    day += d8[j]
            date = datetime.date(int(year), int(month), int(day))
            
            # weekend or not
            eventday = date.weekday()
            weekend = 1 if (eventday == 5 or eventday == 6) else 0

            curr_event = jsonresponse.get(u'_embedded').get(u'events')[i] 
            
            if (curr_event.get(u'classifications')[0] == None or curr_event.get(u'classifications')[0].get(u'genre') == None):
              continue

            city = curr_event.get(u'_embedded').get(u'venues')[0].get(u'city').get(u'name')
            population = getPopulation(city)
            price_max = curr_event.get(u'priceRanges')[0].get(u'max')
            price_min = curr_event.get(u'priceRanges')[0].get(u'min')
            genre = curr_event.get(u'classifications')[0].get(u'genre').get(u'name')

            # not saving this event
            if population == -1 or int(price_min) == 0 or int(price_max) == 0 or genre == 'Undefined':
              continue

            id = curr_event.get('id')
            venue = curr_event.get(u'_embedded').get(u'venues')[0].get(u'name')
            name = curr_event.get(u'name')
            artist_rating = getPopularity(artist)

            show.update({'artist' : artist})
            show.update({'city' : city})
            show.update({'venue' : venue})
            show.update({'showName' : name})
            show.update({'genre' : genre})
            show.update({'weekend' : weekend})
            show.update({'date' : date})
            show.update({'month' : month})
            show.update({'maxprice' : price_max})
            show.update({'minprice' : price_min})
            show.update({'id' : id})
            show.update({'score' : artist_rating})
            show.update({'pop' : population})

            event_id = artist + str(i)
            events.update({event_id : show})
    return events

# returns user's top N artists
def getTopNArtists(N, token):
    if token:
        sp = spotipy.Spotify(auth=token)
        top_artists = sp.current_user_top_artists(limit=N, time_range="medium_term")
    else:
        print("Can't get token!")
    
    artists=[]
    # user's top artists in the past 6 months
    for artist in top_artists["items"]:
        artists.append(artist["name"])
    return artists

# artists = getTopNArtists(10)
artists = getTop100Artists()

masterlist={}
for i in range(0, len(artists)):
# for i in range(500, 1000):
    try:
        print(artists[i])
        dict = getEventsData(artists[i])
        masterlist.update(dict)
    except requests.Timeout as err:
        print('SKIPPED due to TIMEOUT: ' + artists[i])
        continue
    except requests.RequestException as err:
        print(err)
        continue

df = pd.DataFrame.from_dict(masterlist)
df = df.transpose()
df.reset_index(inplace = True, drop = True)

df.to_csv('popdata2.csv', encoding='utf-8')