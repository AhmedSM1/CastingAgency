from models import Movie, Actor, Cast, db
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import dateutil.parser
import babel
import json


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
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()

def updateActorService(actor_id,request_body):
    try:
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        name = request_body.get('name')
        age = request_body.get('age')
        email = request_body.get('email')
        gender = request_body.get('gender')
        phone = request_body.get('phone')
        image_link = request_body.get('image_link')
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
        return jsonify({
                'success': True,
                'actor': actor.format()

        })
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()


def getActorByIdService(actor_id):
    actor = findActor(actor_id)
    return jsonify({
                'success': True,
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender,
                'phone': actor.phone,
                'image_link': actor.image_link,
                "movies": getAllMoviesFromActorId(actor_id)

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
    try:
         actor = findActor(actor_id)
         actor.delete()
         removeActorFromAllMoviesWhenDelete(actor_id)
         return jsonify({
          'success': True,
           'actor id': actor_id
           })
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()
 

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
        print(actor) 
        return actor

def createMovieService(request_body):
    try:
          movie = Movie(request_body['title'], request_body['release_date'], request_body['description'],
                                request_body['genre'] ,request_body['trailer_link'], request_body['poster_link'] )
          movie.insert()
          print("movie was successfully created")

          return jsonify({
                'success': True,
                'movie': movie.format()
            })

    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()



def getMovieByIdService(movie_id):
     movie = findMovie(movie_id)
     return jsonify({
                'success': True,
                'movie': movie.format(),
                "cast": getAllActorInMovie(movie_id)
            })


def paginateMovies(req,list):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * DEFAULT_PAGE_SIZE
    end = start + DEFAULT_PAGE_SIZE
    all_movies = [movie.format() for movie in list]
    return all_movies[start:end]


def getAllMoviesService(req):
    movies = Movie.query.order_by(Movie.id).all()
    paginated_movies = paginateMovies(req, movies)
    if len(movies) == 0:
        abort(404)
    
    return jsonify({
        'success': True,
        'movies': paginated_movies,
        'total_movies': len(movies)
        })



def updateMovieService(movie_id,req):
    try:
         movie= findMovie(movie_id)
         title = req.get('title')
         release_date = req.get('release_date')
         description = req.get('description')
         genre = req.get('genre')
         trailer_link = req.get('trailer_link')
         poster_link = req.get('poster_link')

         if title:
             movie.title = title
         if release_date:
             movie.release_date  = release_date
         if description:
             movie.description = description
         if genre:
             movie.genre = genre
         if trailer_link:
             movie.trailer_link = trailer_link
         if poster_link:
             movie.poster_link = poster_link

         movie.update()
         return jsonify({
                'success': True,
                'movie': movie.format()

           })
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()


def deleteMovieService(movie_id):
    try:
         movie= findMovie(movie_id)
         movie.delete()
         deleteAllActorsWhenMovieDeleted(movie_id)
         return jsonify({
           'success': True,
           'movie_id': movie_id
        })

    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()

def findMovie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404)
    else: 
        return movie
      


def addActorToMovie(movie_id,actor_id):
    try:
         movie = findMovie(movie_id)
         actor = findActor(actor_id)
         cast = Cast.query.filter(Cast.actor_id == actor_id, Cast.movie_id == movie_id).all()
         if not cast:
                cast = Cast(movie_id = movie_id,actor_id = actor_id)
                cast.insert()
                return jsonify({
                        "movie": movie.format(),
                        "actor": actor.format()
                        })
         else:
                abort(409)
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()

def removeActorFromMovie(movie_id,actor_id):
    try:
        movie = findMovie(movie_id)
        actor = findActor(actor_id)
        cast = Cast.query.filter(Cast.actor_id == actor_id, Cast.movie_id == movie_id).all()
        if not cast:
                cast.delete()
                return jsonify({
                        'success': True,
                        'actor id':actor_id,
                        'movie id': movie_id
        })
        else:
              abort(409)
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()
    




def getAllActorInMovie(movie_id):
    try:
        castList =  Cast.query.filter_by(movie_id=movie_id).all()
        actors = []
        for cast in castList:
            actor = Actor.query.get(cast.actor_id)
            actors.append(actor.format())

        if len(actors) > 0:
            return {
            "number of actors": len(actors),
            "actors": actors
             }

    except Exception as e:
        print("Exception occured:  "+ str(e))
            
def getAllMoviesFromActorId(actor_id):
    try:
        castList =  Cast.query.filter_by(actor_id=actor_id).all()
        movies = []
        for cast in castList:
            movie = Movie.query.get(cast.movie_id)
            movies.append(movie.format())
        if len(movies) > 0:
            return {
                "number of movies": len(movies),
                "movies": movies
                }
    except Exception as e:
        print("Exception occured:  "+ str(e))


def deleteAllActorsWhenMovieDeleted(movie_id):
    castList =  Cast.query.filter_by(movie_id=movie_id).all()
    try:
         for cast in castList:
            cast.delete()
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()
    
def removeActorFromAllMoviesWhenDelete(actor_id):
    castList =  Cast.query.filter_by(actor_id=actor_id).all()
    try:
         for cast in castList:
            cast.delete()
    except Exception as e:
        print("Exception occured:  "+ str(e))
        db.session.rollback()
    finally:
        db.session.close()



