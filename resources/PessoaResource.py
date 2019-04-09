from flask_restful import Resource, request
from app.pessoa.Pessoa import Pessoa
from app.pessoa.pessoa_validation import validate


class PessoaResource(Resource):
    def get(self, cpf):
        return vars(Pessoa(**{"nome": 'Renan', "cpf": cpf}))

    def post(self):
        input = request.get_json()

        is_valid, errors = validate(input)

        if not is_valid:
            return errors

        pessoa = Pessoa(**input)
        pessoa.ativar()

        return vars(pessoa)
