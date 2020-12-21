import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, abort
from flask_api import status
from models import Movie, Actor, Cast
from service import create_app, createActorService, getActorByIdService




app = create_app()



@app.after_request
def after_request(response):
  # response.headers.add(
  #     'Access-Control-Allow-Headers',
  #     'Content-Type,Authorization,true')
  response.headers.add(
      'Access-Control-Allow-Methods',
      'GET,PATCH,POST,DELETE,OPTIONS')
  return response


@app.route('/')
def hello():
    return 'works great'


@app.route('/actors', methods=['POST'])
def create_actor():
  request_body =  request.get_json(force=True)
  if not ('name' in request_body and 'age' in request_body and 'email' in request_body and 'phone' in request_body):
      abort(422)

  return createActorService(request_body), status.HTTP_201_CREATED



@app.route('/actors/<int:actor_id>')
def get_actor_by_id(actor_id):
    return getActorByIdService(actor_id), status.HTTP_200_OK



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)