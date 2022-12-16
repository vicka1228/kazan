from flask import Flask, render_template, redirect, request, session, make_response, session, redirect
import time
from sqlalchemy import create_engine
import sqlite3
from flask_restful import Api, Resource, reqparse
import json
import pandas as pd
import requests


# Nothing wrong with:

from backend.concertData import MLDataPoints

# Spotify login and fetch data
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

# Machine Learning
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


# SQL Database

TABLE = 'CONCERTS'
DATABASE = 'DATABASE'

conn = sqlite3.connect(DATABASE, check_same_thread=False)


def save_to_DF(csv_file):
    return pd.read_csv(csv_file)


def save_to_SQL(df):
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS ' + TABLE +
              ' (artist_name text, min_price number)')
    conn.commit()
    df.to_sql(TABLE, conn, if_exists='replace', index=False)


df = save_to_DF('./data.csv')
save_to_SQL(df)


oneh = OneHotEncoder(handle_unknown="ignore")
oneh.fit(df[['month', 'genre', 'artist', 'venue']])


# returns X and y used for ML
# def get_data(df):
  
#   # select features from the dataset
#   X = df[['weekend', 'score', 'month', 'pop', 'genre', 'artist', 'venue']]

#   # encode categorical data
#   X = oneh.transform(X[['month', 'genre', 'artist', 'venue']])

#   # create target variable 
#   y = df['minprice']

#   # convert type to integer
#   y = y.astype('int')
#   return (X, y)

# # split dataframe into train and test
# def split(df):
#   return train_test_split(*get_data(df), test_size = 0.2, random_state = 0)
          
# # predict the min price using Random Forest with bagging
# def train_model(X_train, y_train):

#   # create model with the most optimal number of estimators
#   model = BaggingRegressor(n_estimators = 500)

#   # train the model
#   model.fit(X_train, y_train)
  
#   return model

# X_train, X_test, y_train, y_test = split(df)
# model = train_model(X_train, y_train)



# SPOTIFY API CONNECT & USER LOGIN
SPOTIFY_CLIENT_ID = "d4c88e10069d4bf789bf0d70cb71114a"
SPOTIFY_CLIENT_SECRET = "51dee21966eb485eae0ee1320f731dba"
SCOPE = "user-top-read"
# REDIRECT_URI = "http://localhost:8888/callback/"
# user log in – won't work from .ipynb, download as .py and run
token = util.prompt_for_user_token(scope=SCOPE, client_id=SPOTIFY_CLIENT_ID,
                                   client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=REDIRECT_URI)
# print(token)

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


def getTopNArtists(n):
    if token:
        sp = spotipy.Spotify(auth = token)
        top_artists = sp.current_user_top_artists(limit = n, time_range = "medium_term")
    else:
        print("Can't get token!")
    
    artists=[]
    # user's top artists in the past 6 months
    for artist in top_artists["items"]:
        artists.append(artist["name"])
    return artists

class HelloApiHandler(Resource):
    def get(self):
        print("I am reaching the request")
        return {
            'resultStatus': 'SUCCESS',
            'message': "Hello Api Handler"
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args['type']
        request_json = args['message']
        # ret_status, ret_msg = ReturnData(request_type, request_json)
        # currently just returning the req straight
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"

        final_ret = {"status": "Success", "message": message}

        return final_ret


class ConcertListHandler(Resource):

    def get(self):
        print("I am reaching the request")
        # concerts = pd.read_sql_query(
        #     "SELECT * FROM " + TABLE, conn).to_json(orient="records")
        artists = getTopNArtists(10)
        for artist in artists:
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

        concerts = events.to_json()
        return {
            'resultStatus': 'SUCCESS',
            'message': "Concert List Handler",
            'concerts': concerts
        }


class ArtistListHandler(Resource):
    def get(self):
        print("I am reaching the request")
        # artists = json.dumps((pd.read_sql_query(
        #     "SELECT artist FROM " + TABLE, conn).artist.unique()).tolist())
        artists = json.dumps(getTopNArtists(10))
        return {
            'resultStatus': 'SUCCESS',
            'message': "Artist List Handler",
            'artists': artists
        }


class ConcertInformationHandler(Resource):
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        id = args['id']

        if id:
            # concert_info = pd.read_sql_query(
            #     "SELECT * FROM " + TABLE + " WHERE id = '" + id + "'", conn).to_json(orient="records")
            concert_info = getConcertData(id)

        return {
            'resultStatus': 'SUCCESS',
            'message': "Concert Information Handler",
            'concert_info': concert_info
        }


class SearchHandler(Resource):
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('search-string', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        search_string = args['search-string']
        ans = []
        if search_string:
            for column_name in ['venue', 'artist', 'city', 'showName', 'genre']:
                col = pd.read_sql_query(
                    "SELECT * FROM " + TABLE + " WHERE " + column_name + " LIKE '%" + search_string + "%'", conn)
                if not col.empty:
                    ans = col.to_json(orient="records")

        return {
            'resultStatus': 'SUCCESS',
            'message': "Search Handler",
            'ans': ans
        }


class ConcertsOfArtistHandler(Resource):
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('artist', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        artist = args['artist']

        if artist:
            # concerts = pd.read_sql_query(
            #     "SELECT * FROM " + TABLE + " WHERE artist = '" + artist + "'", conn).to_json(orient = "records")
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
            
            concerts = events.to_json()

        return {
            'resultStatus': 'SUCCESS',
            'message': "Concerts of Artist Handler",
            'concerts': concerts
        }



class ArtistImageHandler(Resource):

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('artist', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        artist = args['artist']
        imageURL = ""

        if artist:
            urlartist = artist.replace(" ", "%20")

            header = {"Authorization": "Bearer " + token}
            searchURL = "https://api.spotify.com/v1/search?q={}&type=artist".format(
                urlartist)

            try:
                resp = requests.get(searchURL, headers=header)
                artist_details = resp.json()
                imageURL = artist_details['artists']['items'][0]['images'][0]['url']
            except TimeoutError:
                print('TimeoutError')

        return {
            'resultStatus': 'SUCCESS',
            'message': "Artist Image Handler",
            'imageURL': imageURL
        }

class ConcertImageHandler(Resource):
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        id = args['id']

        if id:
            # concert_info = pd.read_sql_query(
            #     "SELECT * FROM " + TABLE + " WHERE id = '" + id + "'", conn).to_json(orient="records")
            imageURL = getConcertData(id)['img']

        return {
            'resultStatus': 'SUCCESS',
            'message': "Concert Information Handler",
            'imageURL': imageURL
        }

class PredictionResult(Resource):
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        params = MLDataPoints(args['id'])

        df = pd.DataFrame(params).T
        df.columns = ['weekend', 'score', 'month', 'pop', 'genre', 'artist', 'venue', 'minprice']

        curr_price = df['minprice']
        X = df.drop(['minprice'], axis=1)
        
        X = oneh.transform(X[['month', 'genre', 'artist', 'venue']])
        
        pred_price = model.predict(X)

        if round(pred_price[0], 2) >= curr_price[0]:
            decision = 'BUY. The current price is ' + str(round(pred_price[0], 2) - curr_price[0]) + ' lower than our predicted minimum price. BINGO!'
        else:
            decision = 'WAIT! The current price is ' + str(curr_price[0] - round(pred_price[0], 2)) + ' bigger than our predicted price.'

        return {
            'resultStatus': 'SUCCESS',
            'message': "Decision",
            'decision': decision
        }


CLI_ID = "a506022be18046b9a48be947eb75efb7"
CLI_SEC = "46f709ffe6d9434482efe31d30098684"

API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard
REDIRECT_URI = "http://127.0.0.1:5000/flask/callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True
