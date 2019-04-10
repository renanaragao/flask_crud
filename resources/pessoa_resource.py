from flask_restful import Resource, request
from flask import jsonify
from app.pessoa.validation import PessoaValidation
from app.pessoa.application import PessoaApplication

pessoa_application = PessoaApplication()
pessoa_validation = PessoaValidation()


class PessoaResource(Resource):
    def _resp_400(self, errors):
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    def get(self, cpf):
        find = pessoa_application.get_by_cpf(cpf)

        if find is None:
            resp = jsonify()
            resp.status_code = 404
            return resp

        return find

    def post(self):
        input = pessoa_validation.normalized(request.get_json())

        is_valid, errors = pessoa_validation.validate(input)

        if not is_valid:
            return self._resp_400(errors)

        return pessoa_application.insert(input)

    def put(self, cpf):
        input = pessoa_validation.normalized(request.get_json())

        input["cpf"] = cpf

        is_valid, errors = pessoa_validation.validate(input)

        if not is_valid:
            return self._resp_400(errors)

        pessoa_application.update(input)