import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actor, Movie, Cast
from app import create_app
from decouple import config



class CastingAgencyUnitTesting(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = config('TEST_DATABASE_PATH')

        self.create_actor_request = {
           'name':'Ahmed',
           'age':25,
           'email':'ahmed@Test.com',
           'gender':'male',
           'phone':'+966505558844',
           'image_link':'https://unsplash.com/photos/bbNssNJlsrk'
        }

        self.create_actor_request_missing = {
           'name':'Pedro',
           'age':31,
        }


        self.update_actor_request = {
                "name":"Pedro Pascal"
        }

        self.create_movie_request = {
        "title": "The Good Doctor",
        "release_date": "Friday, December 29, 2017",
        "description": "A young surgeon with Savant syndrome is recruited into the surgical unit of a prestigious hospital. The question will arise: can a person who doesnt have the ability to relate to people actually save their lives?",
        "genre": "drama",
        "trailer_link": "https://youtu.be/fYlZDTru55g",
        "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76"
        }

        self.update_movie_request = {
       "description": "Story about a mafia boss in the 70s",
        "genre": "drama"
        }

        self.update_movie_id = "3"

        self.actor_id = "3"
        self.movie_id = "1"
        self.wrong_movie_id = "9999999"
        self.wrong_actor_id = "9999999"
        self.page = "1"



        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_create_actor(self):
         request = self.client().post('/actors', json= self.create_actor_request)
         data = json.loads(request.data)
         self.assertEqual(request.status_code, 201) 
         self.assertEqual(data['name'], 'Ahmed') 
         self.assertEqual(data['age'], 25) 
         self.assertEqual(data['success'], True)


    def test_400_create_actor(self):
        request = self.client().post('/actors', json= self.create_actor_request_missing)
        self.assertEqual(request.status_code, 400) 
        self.assertEqual(data['success'], False)



    def test_get_actor(self):
        request = self.client().get('/actors/'+self.actor_id)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)

    def test_404_get_actor(self):
        request = self.client().get('/actors/'+self.wrong_actor_id)
        self.assertEqual(request.status_code, 404) 
        self.assertEqual(data['success'], False)


    def test_delete_actor(self):
        request = self.client().delete('/actors/'+self.actor_id)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)

    def test_404_delete_actor(self):
        request = self.client().delete('/actors/'+self.wrong_actor_id)
        self.assertEqual(request.status_code, 404) 
        self.assertEqual(data['success'], False)

    def test_update_actor(self):
        request = self.client().patch('/actors/',json = self.update_actor_request)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['name'], 'Mohammed')
        self.assertEqual(data['success'], True)


    def test_get_all_actors(self):
        request = self.client().get('/actors?page='+self.page)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors']) 


    
    def test_create_movie(self):
        request = self.client().post('/movies',json= movie.to_dict())
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 201) 
        self.assertEqual(data['success'], True)


    def test_get_movie(self):
        request = self.client().get('/movies/'+ self.movie_id)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie']) 

    def test_get_all_movies(self):
        request = self.client().get('/movies?page='+self.page)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies']) 

    def test_update_movie(self):
        request = self.client().patch('/movies/'+ self.update_movie_id, json= self.update_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie']) 







        




if __name__ == "__main__":
    unittest.main()



