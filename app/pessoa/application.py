from app.pessoa.repository import PessoaRepository
from app.pessoa.models import Pessoa

pessoa_repository = PessoaRepository()


class PessoaApplication(object):

    def get_by_cpf(self, cpf):
        return pessoa_repository.get_by_cpf(cpf)

    def insert(self, input):
        pessoa = Pessoa(**input)
        pessoa.ativar()

        pessoa_repository.insert(pessoa)

    def update(self, input):
        pessoa_repository.update(Pessoa(**input))
