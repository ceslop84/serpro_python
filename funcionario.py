"""Classe funcionário, exemplo de herança."""
from pessoa import Pessoa

class Funcionario(Pessoa):
    """Exemplo de uso de herança."""
    def __init__(self, sexo:str, cargo:str, idade: int|None =-1):
        super().__init__(sexo, idade)
        self.cargo = cargo
