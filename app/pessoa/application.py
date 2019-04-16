import app.pessoa.repository as repo
from app.pessoa.models import Pessoa


def get_by_cpf(cpf):
    return repo.get_by_cpf(cpf)


def insert(model):
    pessoa = Pessoa(**model)
    pessoa.ativar()

    repo.insert(pessoa)


def update(model):
    repo.update(Pessoa(**model))
