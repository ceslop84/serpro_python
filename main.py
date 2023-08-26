"""Módulo principal."""
from pessoa import Pessoa
from funcionario import Funcionario

def main():
    """Método main."""
    pessoa = Pessoa("masculio", 37)
    pessoa.metodo_publico()
    pessoa.laco_for()
    pessoa.clausula_if()
    pessoa.clausula_switch()
    pessoa.tratamento_excecao()
    pessoa.documentacao(1, 2.0, "ahhhh")
    pessoa.manipulacao_string("veja isso aqui")
    pessoa.conexao_banco_dados()
    pessoa.escrever_arquivo("teste.txt")
    pessoa.ler_arquivo("teste.txt")
    pessoa.exemplo_retorno_tipado()
    funcionario = Funcionario("masculino", "Engenheiro", 37)
    funcionario.laco_for()
    funcionario.entrada_usuario()

if __name__ == "__main__":
    main()
