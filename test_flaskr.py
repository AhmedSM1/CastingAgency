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
        #self.database_path = os.environ['LOCAL_TEST_DATABASE_PATH']
        self.database_path = 'postgresql://root:rootpwd@localhost:5432/castingAgency_test'

        self.create_actor_request =  {
            "name":"Anya Taylor-Joy",
            "age":24,
            "email":"Anya@Gmail.com",
            "gender":"female",
            "phone":"+9665555555555",
            "image_link":"https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/"
        }


        self.executive_producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB2OFJ6b2pwb1JTUV81dkxHaVJqbSJ9.eyJpc3MiOiJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmYwOGZiY2JiYzRmOTAwNmYyMDEwNmYiLCJhdWQiOiJodHRwczovL2ZzbmRiLWNhc3QtbWd0LmNvbS9hcGkiLCJpYXQiOjE2MTAyMTE3MDEsImV4cCI6MTYxMDIxODkwMSwiYXpwIjoiTGVrTlQ5bTN0WDVQSFd6VVc3UkV4VDZEVjE0VWU2enoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImJhc2ljLXBlcm1pc3Npb24iLCJjcmVhdGU6YWN0b3IiLCJjcmVhdGU6Y2FzdCIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTpjYXN0IiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yLWRldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllLWRldGFpbHMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIl19.IXsu1s_Acbk5NhJKJloXTljQn8m6yPFuZApkU4mmms_2dQnIAqGZQJdnNLDqXkBfMhK2PFs5ZhqE8wdBVakKiu5TEgPUiB-yJpR7-yQqg1-7eQw_kSFE5-F0ShEBj42_ZJ2VKjv9KTMv0WIV926VCqrq89btr2RnwAIMPZOzX4CcfWkkMLjyW4ovLdvj7lXh1JLpHEshOxLIv6M94YB9GVRNEYnWzU0kp2QN6CqW2vHEd-bbptQBde-3GrKxQnMrPWemqRfc3mnF9F4vDIWwjuOS25fsvMFKVzvds6TsH-lU1iqt1vXJP3rBhTAZfHdpKdzb-_n3JAnF9fmezK03FA'
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB2OFJ6b2pwb1JTUV81dkxHaVJqbSJ9.eyJpc3MiOiJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExODE0Mjk3OTU0MTYxMzcyMjA1OCIsImF1ZCI6WyJodHRwczovL2ZzbmRiLWNhc3QtbWd0LmNvbS9hcGkiLCJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTAyMTE1MzEsImV4cCI6MTYxMDIxODczMSwiYXpwIjoiTGVrTlQ5bTN0WDVQSFd6VVc3UkV4VDZEVjE0VWU2enoiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYmFzaWMtcGVybWlzc2lvbiIsImdldDphY3Rvci1kZXRhaWxzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1kZXRhaWxzIiwiZ2V0Om1vdmllcyJdfQ.5x6t0D-Hr0r6dGzSUuKw8GJdgEKimM_XXFDYmJVUG7DDwhtQzB-WyXAKBnNpK4781Yy8ko1yCSokOFku5UX93-wLliPFzOBCxahFG68gs0CpQMHZp6N9jGRHDb5HsTZUORAJPwIgcCyPUHurI2-2pE59bmD9GPN5dNAv21_TrK5Lq0wQgjXxTVtGwkushBgpCr4-MbaYyhEFlR2zzDdBjk4z1dvr7CqrYJGo-0Tu9mSLlpyz1Nb-jQIoDISAnk-ZNIQBspLr6j0m24v4uMZTZ1qWfcaMs4hVRbzSprI3WPB_lNn7iiDyRLWaRzM6PpMBRay-WkhwCfh6HbcY6gqtAw'
        self.casting_assistant_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB2OFJ6b2pwb1JTUV81dkxHaVJqbSJ9.eyJpc3MiOiJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExODE0Mjk3OTU0MTYxMzcyMjA1OCIsImF1ZCI6WyJodHRwczovL2ZzbmRiLWNhc3QtbWd0LmNvbS9hcGkiLCJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTAyMjA0ODAsImV4cCI6MTYxMDMwMDY4MCwiYXpwIjoiTGVrTlQ5bTN0WDVQSFd6VVc3UkV4VDZEVjE0VWU2enoiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYmFzaWMtcGVybWlzc2lvbiIsImdldDphY3Rvci1kZXRhaWxzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1kZXRhaWxzIiwiZ2V0Om1vdmllcyJdfQ.7uhNj4ini5vQxgSPX5PTakJ_0Z-RfhJzdlugKAJqXQcrMW87qG2EERCuEwqox4nYns4GxxfjaSzGfTjaVE_DsdPDQcaUYCsu6OXI_QlmlVzrYwolAdYKDZV8OmzTlhOv-ZM6sK-qdu1K-6baPHc1BMFgV7vSQ7gNq1HfmZ66_w6nTHIvipKIyPKxi3sN5lAkpjL1Fu9OlQL_T9gflyrAYXZxUTKCe2dWRI4YXP9qMPYVHcsFO6Nd_df1QfsZxkqZSXIUsMO6d_XAzw2SHUy5Zx7EsVgA3w2T8JyUL-MF_4MGf4SAM5lSbtxuwNIC-ATGHrI15bf4hqiCeSy-0C-tgA'




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

        self.create_movie_bad_request = {
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

        self.movie_id = "6"
        self.update_movie_id = "4"
        self.get_movie_id = "6"
        self.delete_movie_id = "4"
        self.wrong_movie_id = "9999999"


        self.actor_id = "10"
        self.update_actor_id = "10"
        self.delete_actor_id = "12"
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
         request = self.client().post('/actors', headers={
                                    'Authorization': 'Bearer ' + self.executive_producer_token
                                    }, json= self.create_actor_request)
         data = json.loads(request.data)
         self.assertEqual(request.status_code, 201) 
         self.assertEqual(data['success'], True)


    def test_400_create_actor(self):
        request = self.client().post('/actors',  headers={
                                    'Authorization': 'Bearer ' + self.executive_producer_token
                                    },  json= self.create_actor_request_missing)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 400) 
        self.assertEqual(data['success'], False)

    def test_create_actor_unallowed(self):
            request = self.client().post('/actors', headers={
                                    'Authorization': 'Bearer ' + self.casting_assistant_token
                                    }, json= self.casting_assistant_token)
            data = json.loads(request.data)
            self.assertEqual(request.status_code, 401) 
            self.assertEqual(data['message'],'User does not have enough privileges')
            self.assertEqual(data['success'], False)


    def test_get_actor(self):
        request = self.client().get('/actors/'+self.actor_id, headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)

    def test_404_get_actor(self):
        #not found
        request = self.client().get('/actors/'+self.wrong_actor_id,  headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404) 
        self.assertEqual(data['success'], False)

    def test_401_get_actor(self):
        #unauthorized 
        request = self.client().get('/actors/'+self.wrong_actor_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)



    def test_delete_actor(self):
        request = self.client().delete('/actors/'+self.delete_actor_id,  headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)

    def test_401_delete_actor(self):
        #unauthorized 
        request = self.client().delete('/actors/'+self.actor_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_no_permision_to_delete_actor(self):
        #no permission  
        request = self.client().delete('/actors/'+self.actor_id,  headers={
               'Authorization': 'Bearer ' + self.casting_assistant_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'User does not have enough privileges')
        self.assertEqual(data['success'], False)


    def test_update_actor(self):
        request = self.client().patch('/actors/'+self.update_actor_id,json = self.update_actor_request, headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['name'], 'Mohammed')
        self.assertEqual(data['success'], True)

    def test_no_auth_update_actor(self):
        request = self.client().patch('/actors/'+self.update_actor_id,json = self.update_actor_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)


    def test_no_permission_update_actor(self):
        request = self.client().patch('/actors/'+self.update_actor_id, headers={
               'Authorization': 'Bearer ' + self.casting_assistant_token
        },json = self.update_actor_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'User does not have enough privileges')
        self.assertEqual(data['success'], False)


    def test_404_update_actor(self):
        request = self.client().patch('/actors/'+self.wrong_actor_id, headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        },json = self.update_actor_request )
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data['message'],'resource not found')
        self.assertEqual(data['success'], False) 


    def test_get_all_actors(self):
        request = self.client().get('/actors?page='+self.page,  headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors']) 


    def test_create_movie(self):
        request = self.client().post('/movies', headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
                }, json= self.create_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 201) 
        self.assertEqual(data['success'], True)

    def test_400_create_movie(self):
        request = self.client().post('/movies', headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
                }, json= self.create_movie_bad_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 400) 
        self.assertEqual(data['success'], False)

    def test_401_create_movie(self):
        request = self.client().post('/movies', headers={
               'Authorization': 'Bearer ' + self.casting_assistant_token
                }, json= self.create_movie_request)
        data = json.loads(request.data)        
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'User does not have enough privileges')
        self.assertEqual(data['success'], False)


    def test_no_auth_header_create_movie(self):
        request = self.client().post('/movies', json= self.create_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)        



    def test_get_movie(self):
        request = self.client().get('/movies/'+ self.get_movie_id, headers={
               'Authorization': 'Bearer ' + self.casting_director_token
                })
        data = json.loads(request.data)       
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie']) 


    def test_401_get_movie(self):
        request = self.client().get('/movies/'+ self.get_movie_id)
        data = json.loads(request.data)       
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)    

    def test_get_all_movies(self):
        request = self.client().get('/movies', headers={
               'Authorization': 'Bearer ' + self.casting_director_token
                })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies']) 
        
    def test_401_get_all_movies(self):
        request = self.client().get('/movies')
        data = json.loads(request.data)       
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)    


    def test_update_movie(self):
        request = self.client().patch('/movies/'+ self.update_movie_id, headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
                }, json= self.update_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie']) 

    def test_401_update_movie(self):
        request = self.client().patch('/movies/'+ self.update_movie_id,json= self.update_movie_request)
        data = json.loads(request.data)       
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)    

    def test_delete_movie(self):
        request = self.client().delete('/movies/'+self.delete_movie_id,  headers={
               'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)

    def test_401_delete_movie(self):
        request = self.client().delete('/movies/'+self.movie_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'Authorization header is expected')
        self.assertEqual(data['success'], False)    

    def test_assign_actor_to_movie(self):
        
        request = self.client().patch('/cast/movie/'+ self.movie_id + '/actor/'+ self.actor_id, headers={
               'Authorization': 'Bearer ' + self.casting_director_token
                })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202) 
        self.assertEqual(data['success'], True)

    def test_401_assign_actor_to_movie(self):
        request = self.client().patch('/cast/movie/'+ self.movie_id + '/actor/'+ self.actor_id, headers={
               'Authorization': 'Bearer ' + self.casting_assistant_token
                })
        data = json.loads(request.data)        
        self.assertEqual(request.status_code, 401) 
        self.assertEqual(data['message'],'User does not have enough privileges')
        self.assertEqual(data['success'], False)



        




if __name__ == "__main__":
    unittest.main()



