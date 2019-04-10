from pymongo import MongoClient
from app.pessoa.models import Pessoa

client = MongoClient("mongodb://localhost:27017/")

db = client["pessoa"]


class PessoaRepository(object):
    def __init__(self):
        self.collection = db[Pessoa.__name__]

    def insert(self, model):
        self.collection.insert(vars(model))

    def update(self, model):
        self.collection.replace_one({"cpf": model.cpf}, vars(model))

    def get_by_cpf(self, cpf):
        return self.collection.find_one({"cpf": cpf})