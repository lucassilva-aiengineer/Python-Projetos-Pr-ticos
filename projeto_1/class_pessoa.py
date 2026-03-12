from class_funcoes import Funcoes
from datetime import datetime
from faker import Faker 
import random 
from typing import List, Union
import time

# Desenvolvendo a classe pessoa. 

class Pessoa:

    """Esta classe figura objeto pessoa"""


    def __init__(self, nome: str, data_nascimento: Union[datetime, str], idade: int, cpf: str):

        # Atributos privados 

        self.__id_ = ""
        self.__nome = nome 
        self.__data_nascimento = data_nascimento 
        self.__idade = idade 
        self.__cpf = cpf 


    # Definindo o encapsulamento, algo que é 
    # como a ponte entre o usuário e o atributo e proteje os mesmos, 
    # de uma acesso irregular por parte do atributo. 


    # Os nossos getters, as regras de leitura 

    @property 
    def id_(self)-> str:
        return self.__id_

    @property 
    def nome(self)-> str:
        return self.__nome 

    @property 
    def data_nascimento(self)-> datetime:
        return self.__data_nascimento   

    @property 
    def idade(self)-> int:
        return self.__idade

    @property 
    def cpf(self)-> str:
        return self.__cpf 


    # Os setters, as regras de escrita 

    @id_.setter 
    def id_(self, nv_id: str)-> None:
        self.__id_ = nv_id 

    @nome.setter 
    def nome(self, nv_nome: str)-> None:
        self.__nome = nv_nome 

    @data_nascimento.setter 
    def data_nascimento(self, nv_data_nascimento: datetime)-> None:
        self.__data_nascimento = nv_data_nascimento 

    @idade.setter 
    def idade(self, nv_idade: int)-> None:
        self.__idade = nv_idade

    @cpf.setter 
    def cpf(self, nv_cpf)-> None:
        self.__cpf = nv_cpf 


    # Utilizando um método mágico que permite que 
    # descreve o que será exibido quando o 

    def __repr__(self)-> str:
        return f"""ID: {self.__id_} Nome: {self.__nome}"""



def main():

    # Criando um objeto teste

    def gerar_pessoas(qntd_pessoas: int= 0)-> List[Pessoa]:

        """
            Criando mil pessoas e adicionando estas pessoas 
            a um arquivo txt.  
        """ 

        pessoas: List[Pessoa] = []

        faker = Faker('pt_BR')
        objeto_funcao = Funcoes()

        # Utilizando um operador ternário. 
        pessoas_gerar = qntd_pessoas if  qntd_pessoas else int(input("Indique a quantidade de pessoas que você gostaria de criar: ")) 


        print("Executando código...")

        pessoas_geradas = 0 
        while pessoas_geradas <= pessoas_gerar:

            idade = random.randint(18, 80)

            pessoa = Pessoa(faker.name(), 
                            objeto_funcao.data_nascimento(idade),
                            idade,
                            faker.cpf())

            pessoas.append(pessoa)

            pessoas_geradas += 1

        # Adicionando pessoas a um arquivo txt 

        with open('projeto_1/dados_pessoas.txt', 'w') as file:
            for pessoa in pessoas:

                string = f"{pessoa.id_}, {pessoa.nome}, {pessoa.idade}, {pessoa.cpf}\n"
                file.write(string)

        return pessoas

    try:
        gerar_pessoas(1000)

    except:
        print("Erro encontrado...")
        time.sleep(2)

    # print(gerar_pessoas(10))

    # print("Código executado.")

if __name__ == '__main__':
    main()