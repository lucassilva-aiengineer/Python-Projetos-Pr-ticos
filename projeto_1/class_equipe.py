from __future__ import annotations 
from class_colaborador import Colaborador
from typing import List, Union, Dict, Tuple 
from 


class Equipe:

    equipes: List[Equipe] = []
    # O método construtor 
    def __init__(self, nome_equipe: str= "", nome_lider: str= "", missao_equipe: str= "",
                colaboradores: List[Colaborador]= []):

        # Atributos privados 
        self.__nome_equipe = nome_equipe 
        self.__nome_lider = nome_lider
        self.__missao_equipe = missao_equipe 
        self.__colaboradores = colaboradores 
        self.__custo_operacional_total = 0

    # Definindo as regras de acesso - leitura, os getters 
    @property 
    def nome_equipe(self)-> str:
        return self.__nome_equipe 

    @property 
    def nome_lider(self)-> str:
        return self.__nome_lider 

    @property 
    def missao_equipe(self)-> str: 
        return self.__missao_equipe 

    @property 
    def colaboradores(self)-> List[Colaborador]: 
        return self.__colaboradores 

    @property 
    def custo_operacional_total(self):

        self.__custo_operacional_total = sum([colaborador.salario for colaborador in self.__colaboradores])


    # Defindo as regras de escrita os nossos setter 
    @nome_equipe.setter 
    def nome_equipe(self, nv_nome_equipe: str= "")-> None:

            print("Alterando atributo nome equipe...")
            time.sleep(2)

            senha = input("Indique uma senha: ")

            # Caso o usuário acerte a senha alteramos 
            # o atributo 

            if senha == "ABCD":
                print("Senha correta...")
                time.sleep(2)

                self.__nome_equipe = nv_nome_equipe 
                print("Alteração executada com sucesso!")
                time.sleep(2)

            else: 
                print("Senha inválida!")
                time.sleep(2)


    @nome_lider.setter 
    def nome_lider(self, nv_nome_lider: str= "")-> None:

        pass 


def main():
    pass 



if __name__ == '__main__':
    main()
