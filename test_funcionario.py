"""Classe de teste para funcionário."""
import unittest
from funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    """Classe de teste de funcionário."""

    def test_funcao_funcionario(self):
        """Teste para função de funcionário."""
        funcionario = Funcionario("masculino", "engenheiro")
        observado = funcionario.funcao_para_ser_testada(6,3)
        real = 6 + 3
        self.assertEqual(observado, real)
