from flask import Flask, request, abort, jsonify,url_for, redirect, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_api import status
from models import Movie, Actor, Cast,  db, setup_db
from service import *
from flask_cors import CORS
from auth.auth import AuthError, requires_auth, API_AUDIENCE
from decouple import config
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from dotenv import load_dotenv, find_dotenv
from os import environ as env
import datetime
import jwt

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)



AUTH0_CALLBACK_URL = env['AUTH0_CALLBACK_URL']
AUTH0_CLIENT_ID = env['AUTH0_CLIENT_ID']
AUTH0_CLIENT_SECRET = env['AUTH0_CLIENT_SECRET']
BASE_URL = env['BASE_URL']
LOGOUT_CALLBACK_URL = env['AUTH0_LOGOUT_CALLBACK_URL']
SECRET = env['SECRET']

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={'/': {"origins": "*"}})
  app.secret_key = SECRET
  oauth = OAuth(app)
  auth0 = oauth.register(
    'auth0',
    client_id= AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url= BASE_URL,
    access_token_url= BASE_URL+'/oauth/token',
    authorize_url=BASE_URL + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
  )




  @app.after_request
  def after_request(response):
        response.headers.add(
           'Access-Control-Allow-Headers',
             'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
                'GET,PATCH,POST,DELETE,OPTIONS')
        return response

  @app.route("/")
  def home():
      return "Works great! "


  @app.route('/login')
  def login():
     return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL)
  
  
  @app.route('/logout')
  def logout():
    session.clear()
    params = {'returnTo': LOGOUT_CALLBACK_URL, 'client_id': AUTH0_CLIENT_ID}
    return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params)) 


  @app.route('/callback', methods=['GET'])
  def decode_jwt():
    auth0.authorize_access_token()
    session['access_token'] = auth0.token['access_token']
    session['user_email'] = auth0.get('userinfo').json()['email']
    return redirect(url_for('auth.welcome'))

  @app.route('/welcome')
  @require_auth
  def welcome():
      user_email = session['user_email']
      token = session['access_token']
      return jsonify({
          'email': user_email,
           'token': token
      })



  @app.route('/actors', methods=['POST'])
  @requires_auth('create:actor')
  def create_actor(payload):
        request_body =  request.get_json(force=True)
        if not ('name' in request_body and 'age' in request_body and 'email' in request_body and 'phone' in request_body):
            abort(400)
        return createActorService(request_body), status.HTTP_201_CREATED


  @app.route('/actors/<int:actor_id>')
  @requires_auth('get:actor-details')
  def get_actor_by_id(payload,actor_id):
         return getActorByIdService(actor_id), status.HTTP_200_OK


  @app.route('/actors')
  @requires_auth('get:actors')
  def get_all_actors_per_page(payload):
       return getAllActorService(request), status.HTTP_200_OK


  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actor')
  def delete_actor_by_id(payload,actor_id):
      return deleteActorService(actor_id), status.HTTP_202_ACCEPTED
                            

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('update:actor')
  def update_actor(payload,actor_id):
       request_body = request.get_json()
       return updateActorService(actor_id,request_body), status.HTTP_202_ACCEPTED

  @app.route('/movies', methods=['POST'])
  @requires_auth('create:movie')
  def create_movie(payload):
      request_body = request.get_json()
      if not ('title' in request_body and 'release_date' in request_body and 'description' in request_body and 'genre' in request_body
      and 'poster_link' in request_body):
            abort(400)
      return createMovieService(request_body), status.HTTP_201_CREATED

  
  @app.route('/movies')
  @requires_auth('get:movies')
  def get_all_movies_per_page(payload):
       return getAllMoviesService(request), status.HTTP_200_OK

  
  @app.route('/movies/<int:movie_id>')
  @requires_auth("get:movie-details")
  def get_movies_by_id(payload,movie_id):
       return getMovieByIdService(movie_id), status.HTTP_200_OK

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth("update:movie")
  def update_movie(payload,movie_id):
       request_body = request.get_json()
       return updateMovieService(movie_id,request_body), status.HTTP_202_ACCEPTED

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth("delete:movie")
  def delete_movie_by_id(payload,movie_id):
      return deleteMovieService(movie_id), status.HTTP_202_ACCEPTED

  @app.route('/cast/movie/<int:movie_id>/actor/<int:actor_id>', methods=['PATCH'])
  @requires_auth("create:cast")
  def add_to_movie(payload,movie_id,actor_id):
      return addActorToMovie(movie_id,actor_id), status.HTTP_202_ACCEPTED

  @app.route('/cast/movie/<int:movie_id>/actor/<int:actor_id>', methods=['DELETE'])
  @requires_auth("delete:cast")
  def remove_from_movie(payload,movie_id,actor_id):
      return removeActorFromMovie(movie_id,actor_id), status.HTTP_202_ACCEPTED


  @app.errorhandler(404)
  def notFound(error):
            return jsonify({
                "success": False,
                "error": 404,
                "message": "resource not found"
                 }), 404



  @app.errorhandler(AuthError)
  def auth_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code


  @app.errorhandler(401)
  def unauthorized(error):
        return jsonify({
                "success": False,
                "error": 401,
                "message": 'Unathorized'
            }), 401


  @app.errorhandler(500)
  def internal_server_error(error):
        return jsonify({
                "success": False,
                "error": 500,
                "message": 'Internal Server Error'
            }), 500


  @app.errorhandler(400)
  def bad_request(error):
            return jsonify({
                "success": False,
                "error": 400,
                "message": 'Bad Request'
            }), 400

  return app


app = create_app()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080, debug=True)

