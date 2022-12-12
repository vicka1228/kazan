from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.ApiHandler import HelloApiHandler, ConcertListHandler, ArtistListHandler, ConcertInformationHandler, SearchHandler, ConcertsOfArtistHandler #add all components

app = Flask(__name__, static_url_path='', static_folder='front-end/public')
CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(ConcertListHandler, '/flask/concerts')
api.add_resource(ArtistListHandler, '/flask/artists')
api.add_resource(ConcertInformationHandler, '/flask/concertinfo')
api.add_resource(SearchHandler, '/flask/search')
api.add_resource(ConcertsOfArtistHandler, '/flask/artistconcerts')
