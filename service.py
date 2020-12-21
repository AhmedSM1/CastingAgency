from models import Movie, Actor, Cast, db, setup_db
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_moment import Moment
from flask_cors import CORS
import dateutil.parser
import babel


# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={'/': {"origins": "*"}})

  return app



def createActorService(request_body):
    try:
        actor = Actor(request_body['name'], request_body['age'], request_body['email'], 
                        request_body['gender'] ,request_body['phone'] , request_body['image_link'])
        actor.insert()
        return jsonify({
                'success': True,
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender,
                'phone': actor.phone,
                'image_link': actor.image_link
            })

        print("actor was successfully created")
    except Exception as e:
        print("Exception occured:  "+ e)
        db.session.rollback()
    finally:
        db.session.close()

    
def getActorByIdService(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)
    else: 
        return jsonify({
                'success': True,
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender,
                'phone': actor.phone,
                'image_link': actor.image_link
            })
