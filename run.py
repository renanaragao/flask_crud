from flask import Flask, make_response
from flask_restful import Api
from resources.pessoa_resource import PessoaResource
from resources.auth_resource import AuthResource
from bson.json_util import dumps
from flask_jwt_extended import JWTManager


def output_json(obj, code, headers=None):
    """
    This is needed because we need to use a custom JSON converter
    that knows how to translate MongoDB types to JSON.
    """
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})

    return resp


DEFAULT_REPRESENTATIONS = {'application/json': output_json}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'
app.config['PROPAGATE_EXCEPTIONS'] = True

jwt = JWTManager(app)

api = Api(app, prefix='/api/v1')
api.representations = DEFAULT_REPRESENTATIONS

api.add_resource(PessoaResource, '/pessoa/<int:cpf>', '/pessoa/')
api.add_resource(AuthResource, '/auth/')

if __name__ == '__main__':
    app.run(debug=True)
