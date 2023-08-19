"""Módulo principal."""
from pessoa import Pessoa, Funcionario

def main():
    """Método main."""
    pessoa = Pessoa("masculio", 37)
    pessoa.laco_for()
    pessoa.clausula_if()
    pessoa.clausula_switch()
    pessoa.tratamento_excecao()
    pessoa.conexao_banco_dados()
    pessoa.documentacao(1, 2.0, "ahhhh")
    pessoa.manipulacao_string("veja isso aqui")
    pessoa.escrever_arquivo("teste.txt")
    pessoa.ler_arquivo("teste.txt")
    pessoa.exemplo_retorno_tipado()
    funcionario = Funcionario("masculino", "Engenheiro", 37)
    funcionario.laco_for()

if __name__ == "__main__":
    main()
