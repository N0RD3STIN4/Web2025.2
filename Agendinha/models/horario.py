from datetime import datetime
import json
from models.dao import DAO
class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(0)
        self.set_id_cliente(0)
        self.set_id_servico(0)
        self.set_id_profissional(0)

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    def set_id(self, id): self.__id = id
    def set_data(self, data): 
        agora = datetime.now()
        if data.year < agora.year: raise ValueError('Data inválida (anterior a 2025)')
        self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_json(self):
        dic = {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"),
        "confirmado":self.__confirmado, "id_cliente":self.__id_cliente,
        "id_servico":self.__id_servico, "id_profissional":self.__id_profissional}
        return dic
    
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"

    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_cliente(dic["id_cliente"])
        horario.set_id_servico(dic["id_servico"])
        horario.set_id_profissional(dic["id_profissional"])
        return horario
        
class HorarioDAO(DAO):
    _objetos = []
    arquivo = "horarios.json"
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Horario.to_json)




            