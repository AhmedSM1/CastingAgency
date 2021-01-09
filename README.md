# FSND-Casting-Agency

Udacity Full Stack Nanodegree capstone project - Casting Ageny

## Motivation

This project is the capstone project for `Udacity Full Stack web development nanondegree`.

This project covers all the learnt concepts that were covered by the nanodegree which includes data modeling for web using `postgres`, API development and testing with `Flask`, Authorization with RBAC, `JWT` authentication and finally API deployment using `Heroku`.


## link: https://asm-casting-agency.herokuapp.com/


## Start the project locally

This section will introduce you to how to run and setup the app locally.

### Dependencies

This project is based on `Python 3` and `Flask`.

To install project dependencies:

```bash
$ pip install -r requirements.txt
```
```bash
$ docker-compose up -d 
```
Note: you must have the latest version of Python 3 and Docker 


### Auth0 configs

You need to update auth0_params variable found in `setup.sh` with auth0 configurations

```bash
export FLASK_APP=app
export FLASK_ENV=development
export DATABASE_PATH='postgresql://root:rootpwd@localhost:5432/castingAgency_test'
export LOCAL_TEST_DATABASE_PATH='postgresql://root:rootpwd@localhost:5432/castingAgency_test'
export SECRET='ThisIsTheSecretKey'
export BASE_URL='https://cast-mgt.us.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='https://fsndb-cast-mgt.com/api'
export AUTH0_CLIENT_ID='LekNT9m3tX5PHWzUW7RExT6DV14Ue6zz'
export AUTH0_CALLBACK_URL='https://asm-casting-agency.herokuapp.com/callback'
export AUTH0_LOGOUT_CALLBACK_URL='https://asm-casting-agency.herokuapp.com/login'
```

### Run the app locally

You can run the app using the below commands:

```bash
docker-compose up -d
bash setup.sh
flask run
```

### Run test cases

You can run the unit test cases that are defined in `test_flaskr.py` using the below command:

```bash
python test_app.py
```

## API Documentation

This section will introduce you to API endpoints and error handling


### Error handling

Errors are returned as JSON in the following format:

```json
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```

The API will return the types of errors:

- 400 – bad request
- 404 – resource not found
- 422 – unprocessable
- 500 - internal server error
- 401 - unauthorized

### API Endpoints

<b>Notes</b>
- <b>You need to update the ACCESS_TOKEN in the below requests with JWT valid token.</b>
- <b>The below requests assumes you are running the app locally, so you need to update the requests with the base URL or your URL after deployment.</b>

#### GET /actors

- General: returns a list of all actors
- Sample request:

```bash
curl -X GET http://127.0.0.1:5000/actors -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response:

```json
  "actors": [
        {
            "age": 24,
            "email": "ahmed",
            "gender": "female",
            "id": 1,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "ahmed",
            "phone": "+9665555555555"
        },
        {
            "age": 24,
            "email": "Anya Taylor-Joy",
            "gender": "female",
            "id": 2,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "Anya Taylor-Joy",
            "phone": "+9665555555555"
        },
        {
            "age": 25,
            "email": "ahmed ",
            "gender": "male",
            "id": 3,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "ahmed ",
            "phone": "+9665555555555"
        },
        {
            "age": 65,
            "email": "jackie chan ",
            "gender": "male",
            "id": 4,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "jackie chan ",
            "phone": "+9665555555555"
        },
        {
            "age": 55,
            "email": "phil dunphy",
            "gender": "male",
            "id": 5,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "phil dunphy",
            "phone": "+9665555555555"
        },
        {
            "age": 45,
            "email": "Gloria britchit",
            "gender": "female",
            "id": 6,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "Gloria britchit",
            "phone": "+9665555555555"
        },
        {
            "age": 44,
            "email": "Clare dunphy",
            "gender": "female",
            "id": 7,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "Clare dunphy",
            "phone": "+9665555555555"
        },
        {
            "age": 25,
            "email": "Hailey dunphy",
            "gender": "female",
            "id": 8,
            "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
            "name": "Hailey dunphy",
            "phone": "+9665555555555"
        }
    ],
    "success": true,
    "total_actors": 8
```
#### GET /actors/\<int:actor_id\>

- General: get actors details by id
- Sample request:

```bash
curl -X GET http://127.0.0.1:5000/actors/1 -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response: <i>returns the  actor details</i>

```json
{
    "age": 24,
    "gender": "female",
    "id": 1,
    "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
    "movies": {
        "movies": [
            {
                "description": "Story about a mafia boss in the 50s",
                "genre": "Crime",
                "id": 2,
                "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
                "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
                "title": "Scarface",
                "trailer_link": null
            }
        ],
        "number of movies": 1
    },
    "name": "ahmed",
    "phone": "+9665555555555",
    "success": true
}
```

#### GET /movies

- General: returns a list of all movies
- Sample request:

```bash
curl -X GET http://127.0.0.1:5000/movies -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response:

```json
{
  "movies": [
        {
            "description": "Great story",
            "genre": "Crime",
            "id": 1,
            "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
            "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
            "title": "The god father",
            "trailer_link": null
        },
        {
            "description": "Story about a mafia boss in the 50s",
            "genre": "Crime",
            "id": 2,
            "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
            "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
            "title": "Scarface",
            "trailer_link": null
        },
        {
            "description": "Story about a mafia boss in the 50s",
            "genre": "Crime",
            "id": 3,
            "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
            "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
            "title": "shawshank redemption ",
            "trailer_link": null
        },
        {
            "description": "Story about a fish lost in the oscen",
            "genre": "family",
            "id": 4,
            "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
            "release_date": "Fri, 29 Dec 2000 00:00:00 GMT",
            "title": "Finding nemo",
            "trailer_link": null
        }
    ],
    "success": true,
    "total_movies": 4
}
```
#### GET /movies/\<int:movie_id\>

- General: get movie details by id
- Sample request:

```bash
curl -X GET http://127.0.0.1:5000/movies/2 -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response: <i>returns the  movie details with all the actors inside it </i>

```json
{

    "cast": {
        "actors": [
            {
                "age": 24,
                "email": "ahmed",
                "gender": "female",
                "id": 1,
                "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
                "name": "ahmed",
                "phone": "+9665555555555"
            },
            {
                "age": 25,
                "email": "ahmed ",
                "gender": "male",
                "id": 3,
                "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
                "name": "ahmed ",
                "phone": "+9665555555555"
            },
            {
                "age": 65,
                "email": "jackie chan ",
                "gender": "male",
                "id": 4,
                "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
                "name": "jackie chan ",
                "phone": "+9665555555555"
            },
            {
                "age": 55,
                "email": "phil dunphy",
                "gender": "male",
                "id": 5,
                "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
                "name": "phil dunphy",
                "phone": "+9665555555555"
            }
        ],
        "number of actors": 4
    },
    "movie": {
        "description": "Story about a mafia boss in the 50s",
        "genre": "Crime",
        "id": 2,
        "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
        "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
        "title": "Scarface",
        "trailer_link": null
    },
    "success": true
}
```
#### POST /actors

- General: create a new actor
- Sample request:

```bash
curl -X POST http://127.0.0.1:5000/actors -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN"  -d '{"name":"joe britchit","age":6,"email":"joe@Gmail.com","gender":"male","phone":"+9665555555555","image_link":"https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/"}'
```

- Sample response: <i>returns the new actor id</i>

```json
{
    "age": 6,
    "gender": "male",
    "id": 9,
    "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
    "name": "joe britchit",
    "phone": "+9665555555555",
    "success": true
}
```

#### POST /movies

- General: create a new movie
- Sample request:

```bash
curl -X POST http://127.0.0.1:5000/movies -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{    "title":"Ford vs Ferrari","release_date": "Friday, December 19, 2019","description":"what heepnd to jesse after breaking bad series","genre":"crime","trailer_link":"https://youtu.be/fYlZDTru55g","poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76"}'
```

- Sample response: <i>returns the new movie id</i>

```json
{ "created": 3, "success": true }
```

#### PATCH /actors/\<int:actor_id\>

- General: update an existing actor
- Sample request:
  <i>you can update actor's name, gender and age</i>

```bash
curl -X PATCH http://127.0.0.1:5000/actors/1 -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"name" : "Mohamed Khalaf"}'
```

- Sample response: <i>returns the updated actor object</i>

```json
{
    "movie": {
        "description": "what heepnd to jesse after breaking bad series",
        "genre": "crime",
        "id": 5,
        "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
        "release_date": "Thu, 19 Dec 2019 00:00:00 GMT",
        "title": "Ford vs Ferrari",
        "trailer_link": null
    },
    "success": true
}
```

#### PATCH /movies/\<int:movie_id\>

- General: update an existing movie
- Sample request:
```bash
curl -X PATCH http://127.0.0.1:5000/movies/1 -H "Content-Type: application/json" -H "Authorization: Bearer ACCESS_TOKEN" -d '{"description": "Great story"}'
```

- Sample response: <i>returns the updated movie object which includes the actors acting in this movie</i>

```json
{
    "movie": {
        "description": "Great story",
        "genre": "Crime",
        "id": 1,
        "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
        "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
        "title": "The god father",
        "trailer_link": null
    },
    "success": true
}
```

#### DELETE /actors/\<int:actor_id\>

- General: delete an existing actor
- Sample request:

```bash
curl -X DELETE http://127.0.0.1:5000/actors/2-H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response: <i>returns the deleted actor id</i>

```json
{
    "actor id": 2,
    "success": true
}
```

#### DELETE /movies/\<int:movie_id\>

- General: delete an existing movie
- Sample request:

```bash
curl -X DELETE http://127.0.0.1:5000/movies/1 -H "Authorization: Bearer ACCESS_TOKEN"
```

- Sample response: <i>returns the deleted movie id</i>

```json
{
    "movie_id": 1,
    "success": true
}
```
#### PATCH /cast/movie/\<int:movie_id\>/actor/\<int:actor_id\>


- General: add an actor to a movie
- Sample request:

```bash
curl -X PATCH  http://127.0.0.1:5000/cast/movie/2/actor/1 -H "Authorization: Bearer ACCESS_TOKEN"
```


```json
{

    "actor": {
        "age": 24,
        "email": "Anya Taylor-Joy",
        "id": 1,
        "image_link": "https://www.imdb.com/name/nm5896355/mediaviewer/rm2529043456/",
        "name": "Anya Taylor-Joy",
        "phone": "+9665555555555"
    },
    "movie": {
        "description": "Story about a mafia boss in the 50s",
        "genre": "Crime",
        "id": 2,
        "poster_link": "https://images.app.goo.gl/mG2ARPW22BHbrLo76",
        "release_date": "Mon, 29 Dec 1980 00:00:00 GMT",
        "title": "Scarface",
        "trailer_link": null
    }

}
```

## Authentication and authorization

This API uses Auth0 for authentication, you will need to setup Auth0 application and API. You will need to update auth0_params variable found in config.py.

You can use the below links to setup auth0:

[Auth0 Applications](https://auth0.com/docs/applications)
<br>
[Auth0 APIs](https://auth0.com/docs/api/info)

### Existing user roles



1. Casting Assistant:

- GET /actors (get:actors): can get all actors
- GET /movies (get:movies): can get all movies

2. Casting Director:
- All permissions of `Casting Assistant`
- POST /actors (create:actors): can create new actors
- PATCH /actors (update:actors): can update existing actors
- PATCH /movies (update:movies): can update existing movies
- DELETE /actors (delete:actors): can delete actors from database

3. Exectutive Director:
- All permissions of `Casting Director`
- POST /movies (create:movies): Can create new movies
- DELETE /movies (delete:movies): Can delete movies from database
