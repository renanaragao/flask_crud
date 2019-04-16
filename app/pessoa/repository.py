from pymongo import MongoClient
from app.pessoa.models import Pessoa

client = MongoClient("mongodb://localhost:27017/")

db = client["pessoa"]

collection = db[Pessoa.__name__]


def insert(model):
    collection.insert(vars(model))


def update(model):
    collection.replace_one({"cpf": model.cpf}, vars(model))


def get_by_cpf(cpf):
    return collection.find_one({"cpf": cpf})
