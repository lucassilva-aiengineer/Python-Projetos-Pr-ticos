from class_pessoa  import Pessoa 
from datetime import datetime
from typing import List, Union 

class Colaborador(Pessoa):

    def __init__(self, nome: str= "", data_nascimento: Union[str, datetime]= "", 
                idade: int= 0, cpf: str= "", cargo: str= "", data_admissao: Union[str, datetime]= "",
                descricao_funcao: str= "", relatorios: List[str]= [], salario_atual: float= 0,
                historico_salarial: List[float]= []):

        # Criamos um objeto um padrão. 
        super().__init__(nome, data_nascimento, idade, cpf)

        # Específicamos o nosso objeto 

        # Atributos privados 
        self.__cargo = cargo 
        self.__data_admissao = data_admissao 
        self.__descricao_funcao = descricao_funcao 
        self.__relatorios = relatorios 
        self.__salario = salario_atual 
        self.__historico_salarial = historico_salarial 


    # Encapsulamento - Algo que nos permite estar entre o atributo do objeto e o usuário. 

    # Desenvolvendo os nossos getters. 
    # Os getters são os métodos de acesso, tipo de leitura dos nossos atributos. 
    @property 
    def cargo(self)-> str:

        # veja que é possível exibir ao cliente o atributo que quisermos.
        return self.__cargo 

    @property 
    def data_admissao(self)-> Union[datetime, str]:
        return self.__data_admissao 


    @property 
    def descricao_funcao(self)-> str:
        return self.__descricao_funcao

    @property 
    def relaratorios(self)-> List[str]:
        return self.__relatorios 

    @property 
    def salario(self)-> float:
        return self.__salario 

    @property 
    def historico_salarial(self)-> List[float]:
        return self.__historico_salarial 


    # Deselvolvendo os nossos setters 
    # os nossos métodos de acesso - tipo escrita, alteração.
    # Os nossos setters 

    @cargo.setter 
    def cargo(self, nv_cargo: str)-> None:
        self.__cargo = nv_cargo     


    @data_admissao.setter 
    def data_admissao(self, nv_data_admissao: Union[datetime, str])-> None:
        self.__data_admissao = nv_data_admissao 


    @descricao_funcao.setter 
    def descricao_funcao(self, nv_descricao_funcao: str):
        self.__descricao_funcao.append = nv_descricao_funcao 

    @relaratorios.setter 
    def relatorios(self, nv_relatorios= List[str])-> None:
        self.__relatorios = nv_relatorios

    @salario.setter 
    def salario(self, nv_salario: float)-> None:
        self.__salario = nv_salario 

    @historico_salarial.setter 
    def historico_salarial(self, nv_historico_salarial: List[float])-> None:
        self.__historico_salarial = nv_historico_salarial


    # Criando um método que quando o objeto é impresso 
    # retorna uma string personalizada ao invés de um endereço de 
    # memória, isso através do método mágico __repr__

    def __repr__(self)-> str:
        return  f"""
Nome Colaborador: {self.nome}
Salário Colaborador: {self.__salario}
                """
    def relatorio_colaborador(self)-> str:

        """
            Este método retorna um relatório elaborado 
            sobre o colaborador da empresa.
        """

        return f"""
======================================================
Nome: {self.nome}               Data Nascimento:    {self.data_nascimento}
Cargo: {self.__cargo}   Data Admissão:      {self.__data_admissao}
CPF: {self.cpf}             Idade:  {self.idade}                       
======================================================
Salário: R$ {self.__salario:,.2f}        
Descrição função: {self.__descricao_funcao}

Reclamações e elogios: {[mensao for mensao in self.__relatorios]}"""

def main():

    """
        Testando o objeto colaborador
    """

    colaborador_teste = Colaborador("Marcos")

    # print(colaborador_teste.nome) 

    # Print testando alteração de nome 

    colaborador_teste.nome = "Markus"

    print(colaborador_teste.nome)

    colaborador_teste_a =   Colaborador("Marcos João", 
                                        "25/04/1995", 26, "000.000.000-00", 
                                        "Engenheiro de software", 
                                        "21/06/2020","Lídera uma equipe de software", ["Markus é um ótimo funcionário, muito importante para a empresa."],
                                        25000, [10000, 14000, 21000])

    print(colaborador_teste_a.cpf) 


    print(colaborador_teste_a.relatorio_colaborador())

    print(colaborador_teste_a)

if __name__ == '__main__':
    main()
