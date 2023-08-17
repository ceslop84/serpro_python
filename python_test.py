"""Módulo de testes."""
import unittest
from python import Pessoa

class PessoaTest(unittest.TestCase):
    """Classe de teste unitário."""

    def test_funcao(self):
        """Método de teste."""
        pessoa = Pessoa("masculino")
        obs = pessoa.funcao_para_ser_testada(1,2)
        real = 1+2
        self.assertEqual(obs, real)

if __name__ == '__main__':
    unittest.main()        