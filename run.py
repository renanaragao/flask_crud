from flask import Flask
from flask_restful import Api
from resources.PessoaResource import PessoaResource


app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaResource, '/pessoa/<int:cpf>', '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)
