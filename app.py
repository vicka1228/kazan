from flask import Flask, send_from_directory, redirect, session, request, make_response
import spotipy.util as util
import spotipy
import requests
import json
import time
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from api.ApiHandler import HelloApiHandler, ConcertListHandler, ArtistListHandler, ConcertInformationHandler, SearchHandler, ConcertsOfArtistHandler, ArtistImageHandler  # add all components

app = Flask(__name__, static_url_path='', static_folder='front-end/public')
app.secret_key = "46f709ffe6d9434482efe31d30098684"
CORS(app)  # comment this on deployment

api = Api(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


CLI_ID = "a506022be18046b9a48be947eb75efb7"
CLI_SEC = "46f709ffe6d9434482efe31d30098684"

API_BASE = 'https://accounts.spotify.com'

# Make sure you add this to Redirect URIs in the setting of the application dashboard
REDIRECT_URI = "http://127.0.0.1:8080/flask/callback/"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# Set this to True for testing but you probaly want it set to False in production.
SHOW_DIALOG = True


@app.route("/login")
def verify():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(
        client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI, scope=SCOPE)
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@app.route("/flask/callback/")
def api_callback():
    # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
    sp_oauth = spotipy.oauth2.SpotifyOAuth(
        client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI, scope=SCOPE)
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    # Saving the access token along with all other token related info
    session["token_info"] = token_info

    # print("AAAAAAAAAAAAAAAAAAAA /n AAAAAA \n \n\n\n\n AAAAAAAAAAAA")
    res = make_response(redirect("http://127.0.0.1:3000/home"))
    print(token_info['expires_at'])
    res.set_cookie('token', token_info["access_token"])
    res.set_cookie('expires_at', str(token_info['expires_at']))
    res.set_cookie('refresh_token', token_info['refresh_token'])
    return res


@app.route("/go", methods=['POST'])
def go():
    token_info = request.json
    session['token_info'], authorized = get_token(token_info)
    print(session)
    session.modified = True
    if not authorized:
        return {'redirect': True}
    data = request.form
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    response = sp.current_user_top_tracks(
        limit=data['num_tracks'], time_range=data['time_range'])

    print(json.dumps(response))

    return {"a": "data"}

# Checks to see if token is valid and gets a new token if not


def get_token(session):
    token_valid = False
    token_info = session

    # Checking if the session already has a token stored
    # if not (session.get('token_info', False)):
    #     token_valid = False
    #     return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session['expires_at'] - now < 60

    # Refreshing token if it has expired
    if (is_token_expired):
        # Don't reuse a SpotifyOAuth object because they store token info and you could leak user tokens if you reuse a SpotifyOAuth object
        sp_oauth = spotipy.oauth2.SpotifyOAuth(
            client_id=CLI_ID, client_secret=CLI_SEC, redirect_uri=REDIRECT_URI, scope=SCOPE)
        token_info = sp_oauth.refresh_access_token(
            session['refresh_token'])

    token_valid = True
    return token_info, token_valid


api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(ConcertListHandler, '/flask/concerts')
api.add_resource(ArtistListHandler, '/flask/artists')
api.add_resource(ConcertInformationHandler, '/flask/concertinfo')
api.add_resource(SearchHandler, '/flask/search')
api.add_resource(ConcertsOfArtistHandler, '/flask/artistconcerts')
api.add_resource(ArtistImageHandler, '/flask/artistimage')
