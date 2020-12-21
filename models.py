import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_migrate import Migrate
import json


database_path = 'postgresql://root:rootpwd@localhost:5432/castingAgency'
db = SQLAlchemy()



def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)
    return db


class Movie(db.Model, SerializerMixin):
      __tablename__ = "movies"
      id = Column(db.Integer, primary_key=True)
      title = Column(db.String(120), nullable= False)
      release_date = db.Column(db.DateTime, nullable=False)
      description = db.Column(db.String(500), nullable= True)
      genre = Column(db.String(120), nullable= False)
      trailer_link = db.Column(db.String(500), nullable= True)
      poster_link  = db.Column(db.String(500), nullable= True)

      def __init__(self, title, release_date , description, genre, trailer_link , poster_link):
            self.title = title
            self.release_date = release_date
            self.description = description
            self.genre = genre
            self.trailer_link, trailer_link
            self.poster_link = poster_link
      
      def insert(self):
            db.session.add(self)
            db.session.commit()

      def delete(self):
            db.session.delete(self)
            db.session.commit()
      
      def update(self):
            db.session.commit()





class Actor(db.Model,  SerializerMixin):
      __tablename__ = "actors"
      id = Column(db.Integer, primary_key=True)
      name = Column(db.String(120), nullable= False)
      age = Column(db.Integer, nullable= False)
      email = db.Column(db.String(120), nullable= False)
      gender = Column(db.String(120), nullable= True)
      phone = db.Column(db.String(120), nullable= False)
      image_link = db.Column(db.String(500), nullable= True)

      def __init__(self, name, age, email, gender, phone, image_link):
            self.name = name
            self.age = age
            self.email = email
            self.gender = gender
            self.phone = phone
            self.image_link = image_link

      
      def insert(self):
            db.session.add(self)
            db.session.commit()

      def delete(self):
            db.session.delete(self)
            db.session.commit()
      
      def update(self):
            db.session.commit()




class Cast(db.Model):
     __tablename__ = 'Cast'
     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
     movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
     actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)

     def __init__(self, movie_id, actor_id):
           self.movie_id = movie_id
           self.actor_id = actor_id
          