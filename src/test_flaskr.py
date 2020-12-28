import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actor, Movie, Cast
from app import create_app


class CastingAgencyUnitTesting(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = 'postgresql://root:rootpwd@localhost:5432/castingAgency_test'

        self.actor = {
           'name':'Ahmed',
           'age':25,
           'email':'ahmed@Test.com',
           'gender':'male',
           'phone':'+966505558844',
           'image_link':'https://unsplash.com/photos/bbNssNJlsrk'
        }


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
         actor = Actor(name ='Ahmed',age=25,email='ahmed@Test.com',gender='male',
                        phone='+966505558844',image_link='https://unsplash.com/photos/bbNssNJlsr')

         request = self.client().post('actors', json=actor.to_dict())
         print(request.data)
         print(request)
         data = json.loads(request.data)
         self.assertEqual(request.status_code, 201) 
         self.assertEqual(data['name'], 'Ahmed') 
         self.assertEqual(data['age'], 25) 
         self.assertEqual(data['success'], True)

    def test_get_actor(self):
        request = self.client().get('/actors/1')
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
    
    def test_delete_actor(self):
        request = self.client().delete('/actors/1')
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)

    def test_update_actor(self):
        request = self.client().patch('/actors/1',json = self.new_actor())
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)
        




if __name__ == "__main__":
    unittest.main()



