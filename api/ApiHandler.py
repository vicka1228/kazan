from flask_restful import Api, Resource, reqparse
import json
import pandas as pd

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
    concerts = json.dumps((pd.read_sql_query("SELECT venue FROM " + TABLE, conn).venue.unique()).tolist())
    return {
      'resultStatus': 'SUCCESS',
      'message': "Concert List Handler",
      'concerts': concerts
      }

class ArtistListHandler(Resource):
  def get(self):
    print("I am reaching the request")
    artists = json.dumps((pd.read_sql_query("SELECT artist FROM " + TABLE, conn).artist.unique()).tolist())
    return {
      'resultStatus': 'SUCCESS',
      'message': "Artist List Handler",
      'artists': artists
      }

class ConcertInformationHandler(Resource):
  def post(self):
    print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('venue', type=str)

    args = parser.parse_args()

    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

    venue = args['venue']

    if venue:
      concert_info = pd.read_sql_query("SELECT * FROM " + TABLE + " WHERE venue = '" + venue + "'", conn).to_json()
    
    return {
      'resultStatus': 'SUCCESS',
      'message': "Concert Information Handler",
      'concert_info': concert_info
      }


class SearchHandler(Resource):
  def post(self):
    print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('search_string', type=str)

    args = parser.parse_args()

    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

    search_string = args['search_string']

    if search_string:
      ans = []
      for column_name in ['venue', 'artist', 'city', 'showName', 'genre']:
        ans.append(pd.read_sql_query("SELECT * FROM " + TABLE + " WHERE " + column_name + " LIKE '%" + search_string + "%'", conn))
    
    return {
      'resultStatus': 'SUCCESS',
      'message': "Search Handler",
      'ans': ans.to_json()
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
      concerts = pd.read_sql_query("SELECT * FROM " + TABLE + " WHERE artist = '" + artist + "'", conn).to_json()
    
    return {
      'resultStatus': 'SUCCESS',
      'message': "Search Handler",
      'concerts': concerts
      }

