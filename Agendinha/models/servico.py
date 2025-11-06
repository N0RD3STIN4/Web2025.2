import json
from models.dao import DAO
class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
    
    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): 
        if descricao == "": raise ValueError('Descrição Inválida')
        self.__descricao = descricao
    def set_valor(self, valor): 
        if valor < 0: raise ValueError('Valor inválido')
        self.__valor = valor

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def to_json(self):
        dic = {"id":self.__id, "descricao":self.__descricao, "valor":self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])
    
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor}"
    
class ServicoDAO(DAO):
    _objetos = []
    arquivo = "servicos.json"
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Servico.to_json)