from datetime import datetime, timedelta 


class Funcoes:

    @staticmethod
    def data_nascimento(idade_anos: int)-> datetime:

        hoje = datetime.now()

        return hoje - timedelta(idade_anos * 365)
