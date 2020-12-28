import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort
from flask_api import status
from models import Movie, Actor, Cast,  db, setup_db
from service import createActorService, getActorByIdService, getAllActorService, deleteActorService,updateActorService
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment
from flask_cors import CORS


# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={'/': {"origins": "*"}})


  @app.after_request
  def after_request(response):
     # response.headers.add(
       #     'Access-Control-Allow-Headers',
        #     'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
                'GET,PATCH,POST,DELETE,OPTIONS')
        return response


  @app.route('/actors', methods=['POST'])
  def create_actor():
        request_body =  request.get_json(force=True)
        if not ('name' in request_body and 'age' in request_body and 'email' in request_body and 'phone' in request_body):
            abort(422)
        return createActorService(request_body), status.HTTP_201_CREATED

  @app.route('/')
  def hello():
     return 'works great'


  @app.route('/actors/<int:actor_id>')
  def get_actor_by_id(actor_id):
         return getActorByIdService(actor_id), status.HTTP_200_OK



  @app.route('/actors')
  def get_all_actors_per_page():
       return getAllActorService(request), status.HTTP_200_OK


  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  def delete_actor_by_id(actor_id):
      return deleteActorService(actor_id), status.HTTP_202_ACCEPTED
                            

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  def update_actor(actor_id):
       request_body = request.get_json()
       return updateActorService(actor_id,request_body), status.HTTP_202_ACCEPTED






  @app.errorhandler(404)
  def notFound(error):
            return jsonify({
                "success": False,
                "error": 404,
                "message": "resource not found"
                 }), 404



    # @app.errorhandler(AuthError)
    # def auth_error(error):
    #     return jsonify({
    #         "success": False,
    #         "error": error.status_code,
    #         "message": error.error['description']
    #     }), error.status_code


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

