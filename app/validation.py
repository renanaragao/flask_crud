from cerberus import Validator


_schema = {
    'auth': {
        'username': {
            'type': 'string',
            'maxlength': 50,
            'required': True
        },
        'password': {
            'type': 'string',
            'required': True
        }
    },
    'Pessoa': {
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
}


def validate(document, schema):
    validator = Validator(_schema[schema], purge_unknown=True, allow_unknown=False)

    normalized = validator.normalized(document)

    return validator.validate(normalized), validator.errors, normalized

