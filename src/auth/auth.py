import json
from flask import request, _request_ctx_stack, abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen
import os
from decouple import config



BASE_URL = config('BASE_URL')
ALGORITHMS = config('ALGORITHMS')
API_AUDIENCE = config('API_AUDIENCE')


class AuthError(Exception):

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code




def get_token_auth_header():
    """
      Obtains the access token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected"
            }, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must start with"
                               " Bearer"
            }, 401)
    elif len(parts) == 1:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Token not found"
            }, 401)
    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be"
                               " Bearer token"
            }, 401)

    return parts[1]



def check_permissions(permission, payload):
    if payload.get('permissions'):
        print("permission exist")
        token_scopes = payload.get("permissions")
        if permission not in token_scopes:
            raise AuthError(
                {
                    'code': 'invalid_permissions',
                    'description': 'User does not have enough privileges'
                }, 401)
        else:
            return True
    else:
        print("permission doesnt exist")
        raise AuthError(
            {
                'code': 'invalid_permissions',
                'description': 'User does not have any roles attached'
            }, 401)



def verify_decode_jwt(token):
    # verify the token using Auth0 /.well-known/jwks.json
    jsonurl = urlopen(BASE_URL+'/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError(
            {
                'code': 'invalid_header',
                'description': 'Authorization malformed.'
            }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(token,
                                 rsa_key,
                                 algorithms=ALGORITHMS,
                                 audience=API_AUDIENCE,
                                 issuer=BASE_URL + '/')

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {
                    'code': 'token_expired',
                    'description': 'Token expired.'
                }, 401)

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    'code':
                        'invalid_claims',
                    'description':
                        'Incorrect claims. Please, check the audience and issuer.'
                }, 401)
        except Exception:
            raise AuthError(
                {
                    'code': 'invalid_header',
                    'description': 'Unable to parse authentication token.'
                }, 400)
    raise AuthError(
        {
            'code': 'invalid_header',
            'description': 'Unable to find the appropriate key.'
        }, 400)


'''
@TODO implement @requires_auth(permission) decorator method
    @INPUTS
        permission: string permission (i.e. 'post:drink')
    it should use the get_token_auth_header method to get the token
    it should use the verify_decode_jwt method to decode the jwt
    it should use the check_permissions method validate claims and check the requested permission
    return the decorator which passes the decoded payload to the decorated method
'''


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            print(payload)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator