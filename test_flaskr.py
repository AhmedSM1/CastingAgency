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
        self.database_path = os.environ['LOCAL_TEST_DATABASE_PATH']

        self.create_actor_request = {
            "name": "Anya Taylor-Joy",
            "age": 24,
            "email": "Anya@Gmail.com",
            "gender": "female",
            "phone": "+9665555555555",
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/"
        }

        self.executive_producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB2OFJ6b2pwb1JTUV81dkxHaVJqbSJ9.eyJpc3MiOiJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmYwOGZiY2JiYzRmOTAwNmYyMDEwNmYiLCJhdWQiOiJodHRwczovL2ZzbmRiLWNhc3QtbWd0LmNvbS9hcGkiLCJpYXQiOjE2MTAyMzIzNDQsImV4cCI6MTYxMDMxMjU0NCwiYXpwIjoiTGVrTlQ5bTN0WDVQSFd6VVc3UkV4VDZEVjE0VWU2enoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImJhc2ljLXBlcm1pc3Npb24iLCJjcmVhdGU6YWN0b3IiLCJjcmVhdGU6Y2FzdCIsImNyZWF0ZTptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTpjYXN0IiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9yLWRldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllLWRldGFpbHMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIl19.v2bWNuCBe5HS3fPwYmm6SkNQifYoYgidDqXHFEiFrQlTvuEn73lZh-gbPEpFeTqYK6gd0iq-BalhnI_IhV3CLmj_xfhDKOSxtzFFRFd4IgsFHY1rAwcZhrATO1bb3aQTK2G-h9ZL5B88BUWc53JJxMNYBwiOXqsv1itW9FM6N-KbRN8xzI09Dtyeg_Nj16-d1UpMKzAmruKhVZun6BBU5plTmszgAJKwUQ9i59s1Q0jiLdhbbgWcti6LeknphVnD8irCOB9Yibt-riOxGF6UieaxrXMr8gWFeyV2PgtlKcPXY_X5f2bP7JuRbHepRU-ZTcmzD5vmmmrKZXsW4g0yQA'
        self.casting_director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB2OFJ6b2pwb1JTUV81dkxHaVJqbSJ9.eyJpc3MiOiJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmY5Yjk0NmU1NWNmYTAwNzVmYzQ3ODgiLCJhdWQiOiJodHRwczovL2ZzbmRiLWNhc3QtbWd0LmNvbS9hcGkiLCJpYXQiOjE2MTAyMzIxNjksImV4cCI6MTYxMDMxMjM2OSwiYXpwIjoiTGVrTlQ5bTN0WDVQSFd6VVc3UkV4VDZEVjE0VWU2enoiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImJhc2ljLXBlcm1pc3Npb24iLCJjcmVhdGU6YWN0b3IiLCJjcmVhdGU6Y2FzdCIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTpjYXN0IiwiZ2V0OmFjdG9yLWRldGFpbHMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllLWRldGFpbHMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIl19.FaBJ6hlcUXZm7_Ilf9dIjFTL-0poKzW4SH0bllqSrrSFsxbMSG8cI2RDtkdKDZ6SSq-IFv0IFts8_lNjBvN3bPyeqb0VUr1KxuTOc4ajT-VRKsTbWa546mKFR_lYel-_OcjWLFcOMBQdrF61zLm-FZ3QAtj5NlIcnLldgPZfJk-Ck-dS640isphhK_-J6fGoQ9ZTQDDugFdaySXGXEt0LGKRVwZabvYVN3S3tZlHOKWHqSZURl6ggJW9p3pny3V8hIsOwlh9Sj_JXOaT8VUJ5NPlGrRfTGzqXA8aCnlu9XwZkNOwlgJJyDRZYIrWT0l0I5SeL2nOSN50LJEnCWek2'
        self.casting_assistant_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlB2OFJ6b2pwb1JTUV81dkxHaVJqbSJ9.eyJpc3MiOiJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExODE0Mjk3OTU0MTYxMzcyMjA1OCIsImF1ZCI6WyJodHRwczovL2ZzbmRiLWNhc3QtbWd0LmNvbS9hcGkiLCJodHRwczovL2Nhc3QtbWd0LnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MTAyMzIwNzgsImV4cCI6MTYxMDMxMjI3OCwiYXpwIjoiTGVrTlQ5bTN0WDVQSFd6VVc3UkV4VDZEVjE0VWU2enoiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYmFzaWMtcGVybWlzc2lvbiIsImdldDphY3Rvci1kZXRhaWxzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZS1kZXRhaWxzIiwiZ2V0Om1vdmllcyJdfQ.hJ1Cc-l_jJ9o1Dstaq0AGkTzJqJ0OUev3yiPaKiWHOQ9uNUYGOppiCKW_eF0t1K6Lu7xRyGtM-bJ0zs8k6w8qYajc_-86UOxoi3vDY32f-M49xVENO1HuhG_gd1zE7UM3cEy7zNYZnHspI4ZD2Ylen0hnBZ6Pf5wmRr-Rbb_kZZeX0AX3Kgh7j3i-t8dANWqLGt0UL0uwbLbaVdO1v0b8KkQBxZGPLImYgv5HWS0AMNygTaAFAqwyWAmNnuWPT-PDgixTjJkALr43Yp9d7Jw2Mwmvrkc-yLWRh_ECpC201z4qL35UdALne-yajk8IPCWzXEiHPVXUC6dulzWkspkHw'

        self.create_actor_request_missing = {
            'name': 'Pedro',
            'age': 31,
        }

        self.update_actor_request = {
            "name": "Pedro Pascal"
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

        self.movie_id = "1"
        self.update_movie_id = "2"
        self.get_movie_id = "2"
        self.delete_movie_id = "4"
        self.wrong_movie_id = "9999999"

        self.actor_id = "10"
        self.update_actor_id = "10"
        self.delete_actor_id = "1"
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
        }, json=self.create_actor_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_400_create_actor(self):
        request = self.client().post('/actors', headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        }, json=self.create_actor_request_missing)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_create_actor_unallowed(self):
        request = self.client().post('/actors', headers={
            'Authorization': 'Bearer ' + self.casting_assistant_token
        }, json=self.casting_assistant_token)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'User does not have enough privileges')
        self.assertEqual(data['success'], False)

    def test_get_actor(self):
        request = self.client().get('/actors/' + self.actor_id, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_get_actor(self):
        # not found
        request = self.client().get('/actors/' + self.wrong_actor_id, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_401_get_actor(self):
        # unauthorized
        request = self.client().get('/actors/' + self.wrong_actor_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        request = self.client().delete('/actors/' + self.delete_actor_id, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202)
        self.assertEqual(data['success'], True)

    def test_401_delete_actor(self):
        # unauthorized
        request = self.client().delete('/actors/' + self.actor_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_no_permision_to_delete_actor(self):
        # no permission
        request = self.client().delete('/actors/' + self.actor_id, headers={
            'Authorization': 'Bearer ' + self.casting_assistant_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'User does not have enough privileges')
        self.assertEqual(data['success'], False)

    def test_update_actor(self):
        request = self.client().patch('/actors/' + self.update_actor_id, json=self.update_actor_request, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202)
        self.assertEqual(data['name'], 'Mohammed')
        self.assertEqual(data['success'], True)

    def test_no_auth_update_actor(self):
        request = self.client().patch('/actors/' + self.update_actor_id, json=self.update_actor_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_no_permission_update_actor(self):
        request = self.client().patch('/actors/' + self.update_actor_id, headers={
            'Authorization': 'Bearer ' + self.casting_assistant_token
        }, json=self.update_actor_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'User does not have enough privileges')
        self.assertEqual(data['success'], False)

    def test_404_update_actor(self):
        request = self.client().patch('/actors/' + self.wrong_actor_id, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        }, json=self.update_actor_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_get_all_actors(self):
        request = self.client().get('/actors?page=' + self.page, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_create_movie(self):
        request = self.client().post('/movies', headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        }, json=self.create_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 201)
        self.assertEqual(data['success'], True)

    def test_400_create_movie(self):
        request = self.client().post('/movies', headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        }, json=self.create_movie_bad_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_401_create_movie(self):
        request = self.client().post('/movies', headers={
            'Authorization': 'Bearer ' + self.casting_assistant_token
        }, json=self.create_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'User does not have enough privileges')
        self.assertEqual(data['success'], False)

    def test_no_auth_header_create_movie(self):
        request = self.client().post('/movies', json=self.create_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_get_movie(self):
        request = self.client().get('/movies/' + self.get_movie_id, headers={
            'Authorization': 'Bearer ' + self.casting_director_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_401_get_movie(self):
        request = self.client().get('/movies/' + self.get_movie_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
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
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_update_movie(self):
        request = self.client().patch('/movies/' + self.update_movie_id, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        }, json=self.update_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_401_update_movie(self):
        request = self.client().patch('/movies/' + self.update_movie_id, json=self.update_movie_request)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        request = self.client().delete('/movies/' + self.delete_movie_id, headers={
            'Authorization': 'Bearer ' + self.executive_producer_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202)
        self.assertEqual(data['success'], True)

    def test_401_delete_movie(self):
        request = self.client().delete('/movies/' + self.movie_id)
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'Authorization header is expected')
        self.assertEqual(data['success'], False)

    def test_assign_actor_to_movie(self):
        request = self.client().patch('/cast/movie/' + self.movie_id + '/actor/' + self.actor_id, headers={
            'Authorization': 'Bearer ' + self.casting_director_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 202)
        self.assertEqual(data['success'], True)

    def test_401_assign_actor_to_movie(self):
        request = self.client().patch('/cast/movie/' + self.movie_id + '/actor/' + self.actor_id, headers={
            'Authorization': 'Bearer ' + self.casting_assistant_token
        })
        data = json.loads(request.data)
        self.assertEqual(request.status_code, 401)
        self.assertEqual(data['message'], 'User does not have enough privileges')
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
