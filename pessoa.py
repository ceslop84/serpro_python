"""Módulo de estudo de python."""
import sqlite3
import datetime

class Pessoa:
    """Classe pessoa em python.""" 
    def __init__(self, sexo:str, idade=-1,):
        self.idade = idade
        self.sexo = sexo

    @property
    def idade(self) -> int:
        """Método getter para idade."""
        return self._idade

    @idade.setter
    def idade(self, valor):
        """Método setter para idade."""
        self._idade = valor

    @property
    def sexo(self) -> str:
        """Método getter para sexo."""
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        """Método setter para sexo."""
        self._sexo = valor

    def _metodo_protected(self):
        print("Idade", self.idade)

    def __metodo_privado(self):
        print("Sexo", self.sexo)

    def metodo_publico(self):
        """Método público."""
        self._metodo_protected()
        self.__metodo_privado()

    def laco_for(self):
        """Laço for."""
        for i in range(10):
            print(i)
        lista = [1,2,3,4,5]
        for i in lista:
            print(i)
        dicionario = {"nome": "Cesar", "idade": 37, "sexo": "masculino"}
        for key, value in dicionario.items():
            print(key, value)

    def clausula_if(self):
        """Cláusula if."""  
        if self.idade > 65:
            print("Maior de 65 anos.")
        elif self.idade < 18:
            print("Menos de 18 anos.")
        else:
            print("Adulto.")

    def clausula_switch(self):
        """Cláusula switch."""
        match self.sexo:
            case "masculino":
                print("É homem.")
            case "feminino":
                print("É mulher.")
            case _:
                print("Não previsto!")

    def tratamento_excecao(self):
        """Tratamento de exceções."""
        try:
            print("Tentando resolver algo...")
            raise NotImplementedError()
        except NotImplementedError as exp1:
            print("Peguei a exceção!", exp1)
        finally:
            print("Isso aqui sempre vai ser tratado!")

    def documentacao(self, param1:int, param2:float, param3:str) -> str:
        """
        Método exemplo dedocumentação.

        Parameters:

            param1 (int): número inteiro.
            param2 (float): número decimal.
            param3 (str): texto.
        
        Returns (str): texto processado
        """
        return f"{param1} e {param2} e {param3}"

    def conexao_banco_dados(self):
        """Método para conexão ao banco de dados."""   

        try:
            connection = sqlite3.connect("database.db")
        except Exception as exp1: #pylint: disable=broad-exception-caught
            print("Algo deu errado", exp1)
            return
        with connection:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS movie")
            cursor.execute("CREATE TABLE movie(title, year, score)")
            data1 = ['Monty Python and the Holy Grail', 1975, 8.2]
            data2 = ['And Now for Something Completely Different', 1971, 7.5]
            cursor.execute("INSERT INTO movie VALUES (?, ?, ?)", data1)
            cursor.execute("INSERT INTO movie VALUES (?, ?, ?)", data2)
            cursor.execute("DELETE FROM movie WHERE year=?", [1975])
            cursor.execute("UPDATE movie SET year = ? WHERE year = ?", [1984, 1971])
            result = cursor.execute("SELECT * FROM movie")
            rows = result.fetchall()
            for row in rows:
                print (row)

    def manipulacao_string(self, texto:str):
        """Método para manipulação de strings."""
        print("Primeiros 5 caracteres: ", texto[:5])
        print(f"Esta string tem {len(texto)} caracteres.")
        print(f"Em caixa baixa: {texto.lower()}")
        print(f"Em caixa ALTA: {texto.upper()}")
        print(f"Substituindo: {texto.replace('a', 'b')}")
        print(f"Split: {texto.split(' ')}")

    def funcao_para_ser_testada(self, valor1:int, valor2:int) -> int:
        """Função para ser testada."""
        return valor1 + valor2

    def escrever_arquivo(self, nome_arquivo:str):
        """Método para escrever em arquivo."""
        conteudo_lista = [1,2,3,4,5,6,7,8,9,10]
        conteudo_dicionario = {"nome": "teste", "idade": 37}

        # r - read, a - append, w - write, x - create
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            for linha in conteudo_lista:
                arquivo.write(f"{linha}\n")
            for key, value in conteudo_dicionario.items():
                arquivo.write(f"{key}: {value}\n")

    def ler_arquivo(self, nome_arquivo:str):
        """Método para ler arquivos."""  
        # r - read, a - append, w - write, x - create
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
            for linha in conteudo:
                print(linha)

    def exemplo_retorno_tipado(self) -> str:
        """Exemplo de retorno tipado."""
        return "Exemplo de retorno tipado como string."

    def entrada_usuario(self):
        """Método para capturar entrada de dados do usuário."""
        texto = input("Entrar com o dado de teste:")
        print(f"O texto de entrada é: {texto}")

    def manipulacao_data(self, data: str):
        """Método para manipulação de datas."""
        agora = datetime.datetime.now()
        print("Parâmetros de hoje", agora.year, agora.month, agora.day,
              agora.hour, agora.minute, agora.second)
        print("Agora formatado: ", agora.strftime("%Y-%m-%d"))
        timedelta = datetime.timedelta(weeks=1)
        print("Daqui uma semana: ", (agora+timedelta).strftime("%Y-%m-%d"))
        timedelta = datetime.timedelta(days=1)
        print("Daqui 30 dias: ", (agora+timedelta).strftime("%Y-%m-%d"))
        final_ano = datetime.date(2023, 12, 31)
        diff = final_ano - datetime.date.today()
        print("Dias para o final do ano: ", diff.days)
        data_list = [int(d) for d in data.split("/")]
        data_informada = datetime.date(data_list[2], data_list[1], data_list[0])
        print("Data informada: ", data_informada.strftime("%d/%m/%Y"))
