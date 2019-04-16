import flask_restful
from flask import jsonify
from flask_jwt_extended import jwt_required
from app.validation import *
import app.pessoa.application as application


def _resp_400(errors):
    resp = jsonify(errors)
    resp.status_code = 400
    return resp


class PessoaResource(flask_restful.Resource):

    @jwt_required
    def get(self, cpf):
        find = application.get_by_cpf(cpf)

        if find is None:
            resp = jsonify()
            resp.status_code = 404
            return resp

        return find

    @jwt_required
    def post(self):
        pessoa = flask_restful.request.get_json()

        is_valid, errors, normalized = validate(pessoa, schema='Pessoa')

        if not is_valid:
            return _resp_400(errors)

        return application.insert(normalized)

    @jwt_required
    def put(self, cpf):
        pessoa = flask_restful.request.get_json()

        pessoa["cpf"] = cpf

        is_valid, errors, normalized = validate(pessoa, schema='Pessoa')

        if not is_valid:
            return _resp_400(errors)

        application.update(normalized)
