from models import Movie, Actor, Cast, db
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import dateutil.parser
import babel


DEFAULT_PAGE_SIZE = 10

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

def updateActorService(actor_id,request_body):
    try:
        actor = findActor(actor_id)
        name = body.get('name')
        age = body.get('age')
        email = body.get('email')
        gender = body.get('gender')
        phone = body.get('phone')
        image_link = body.get('image_link')
        if name:
            actor.name = name
        if age:
            actor.age = age
        if email:
            actor.email = email
        if gender:
            actor.gender = gender
        if phone:
            actor.phone = phone
        if image_link:
            actor.image_link = image_link

        actor.update()
    except BaseException:
        abort(400)

    return jsonify({
                'success': True,
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender,
                'phone': actor.phone,
                'image_link': actor.image_link
        })


def getActorByIdService(actor_id):
    actor = findActor(actor_id)
    return jsonify({
                'success': True,
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender,
                'phone': actor.phone,
                'image_link': actor.image_link
            })


def getAllActorService(req):
    actors = Actor.query.order_by(Actor.id).all()
    paginated_actors = paginateActors(req,actors)
    if len(actors) == 0:
        abort(404)
    
    return jsonify({
        'success': True,
        'actors': paginated_actors,
        'total_actors': len(actors)
        })
    
def deleteActorService(actor_id):
    actor = findActor(actor_id)
    actor.delete()
    return "actor with id: "+ str(actor_id) +" was succeffully deleted"

def updateActorService(actor_id,request_body):
    actor = findActor(actor_id)
    
    

def paginateActors(req,list):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * DEFAULT_PAGE_SIZE
    end = start + DEFAULT_PAGE_SIZE
    all_actors = [actor.format() for actor in list]
    return all_actors[start:end]


def findActor(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)
    else: 
        return actor



# def createMovieService(request_body):



#TODO unit testing for actor
#TODO Create,update,delete Movie
#TODO Add Actor in a movie
#TODO unit test for movies

