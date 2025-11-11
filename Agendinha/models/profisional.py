import json
from models.dao import DAO


class Profissional:
    def __init__(self, id, nome, email, especialidade, conselho, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_senha(senha)

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_especialidade(self):
        return self.__especialidade

    def get_conselho(self):
        return self.__conselho

    def get_senha(self):
        return self.__senha

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        if nome == "":
            raise ValueError("Nome inválido")
        self.__nome = nome

    def set_email(self, email):
        if email == "":
            raise ValueError("E-mail inválido")
        self.__email = email

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    def set_conselho(self, conselho):
        self.__conselho = conselho

    def set_senha(self, senha):
        if senha == "":
            raise ValueError("Senha inválida")
        self.__senha = senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__especialidade} - {self.__conselho}"

    def to_json(self):
        dic = {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "senha": self.__senha,
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Profissional(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["especialidade"],
            dic["conselho"],
            dic["senha"],
        )


class ProfissionalDAO(DAO):
    _objetos = []
    arquivo = "profissionais.json"

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("profissionais.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Profissional.to_json)
