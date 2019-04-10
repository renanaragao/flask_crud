from cerberus import Validator

class PessoaValidation(object):
    def __init__(self):
        self._schema = {
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
        self.validator = Validator(self._schema, purge_unknown=True, allow_unknown=False)

    def validate(self, document):
        return self.validator.validate(document), self.validator.errors

    def normalized(self, document):
        return self.validator.normalized(document)
