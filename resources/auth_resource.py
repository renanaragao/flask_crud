from flask import jsonify

from app.auth.auth import *
from flask_jwt_extended import create_access_token
from app.validation import validate
import flask_restful


class AuthResource(flask_restful.Resource):

    def post(self):

        user = flask_restful.request.get_json()

        is_valid, errors = validate(user, schema='auth')

        if not is_valid:
            resp = jsonify(errors)
            resp.status_code = 400
            return resp

        result = verify(**user)

        if result:
            token = create_access_token(identity=result.id)

            return {'access_token': token}, 200

        return {'msg': 'Login or password invalid'}, 401
