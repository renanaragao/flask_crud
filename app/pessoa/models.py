class Pessoa:
    def __init__(self, nome, cpf):
        self.ativo = False
        self.nome = nome
        self.cpf = cpf

    def ativar(self):
        self.ativo = True
