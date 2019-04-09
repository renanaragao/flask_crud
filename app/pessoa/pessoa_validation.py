from cerberus import Validator

_schema = {
    'nome': {
        'type': 'string',
        'maxlength': 50,
        'required': True
    },
    'cpf': {
        'type': 'integer',
        'required': True
    }
}


def validate(document):

    v = Validator(_schema)

    return v.validate(document), v.errors
