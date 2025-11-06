from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profisional import Profissional, ProfissionalDAO
import datetime

class View:
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return 
        View.cliente_inserir("admin", "admin", "fone", "1234")
    # def cliente_atualizar_senha_admin():
    
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha: return {"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha: return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def cliente_inserir(nome, email, fone, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email: raise ValueError('E-mail já cadastrado')
        for obj in View.profissional_listar():
            if obj.get_email() == email: raise ValueError('E-mail já cadastrado')
        # if email == 'admin': raise ValueError('E-mail já cadastrado')
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        for obj in View.cliente_listar():
            if obj.get_id() != id and obj.get_email() == email: raise ValueError('E-mail já cadastrado')
        for obj in View.profissional_listar():
            if obj.get_email() == email: raise ValueError('E-mail já cadastrado')
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_cliente() == id: raise ValueError('Cliente já agendado, não é possível excluir')
        cliente = Cliente(id, 'sem nome', 'sem email', 'sem telefone', 'sem senha')
        ClienteDAO.excluir(cliente)
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
 
    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key = lambda obj : obj.get_descricao())
        return r
    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError('Serviço já cadastrado')
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao: raise ValueError('Descrição já cadastrada em outro serviço')
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_servico() == id: raise ValueError('Serviço já agendado, não é possível excluir')
        servico = Servico(id, "sem descrição", 0 )
        ServicoDAO.excluir(servico)
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico

    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        for obj in View.horario_listar():
            if obj.get_id()!= id and obj.get_data() == data and obj.get_id_profissional() == id_profissional: raise ValueError('Horário já cadastrado para esse profissional')
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)
    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key = lambda obj : obj.get_data())
        return r
    def horario_listar_id(id):
        horario = HorarioDAO.listar_id(id)
        return horario
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        for obj in View.horario_listar():
            if obj.get_id()!= id and obj.get_data() == data and obj.get_id_profissional() == id_profissional: raise ValueError('Horário já cadastrado para esse profissional')
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id() == id and obj.get_id_cliente() != None: raise ValueError('Não é possível excluir, horário já cadastrado')
        data = datetime.datetime.now()
        c = Horario(id, data)
        HorarioDAO.excluir(c)
    def horario_agendar_horario(id_profissional):
        r = [] 
        agora = datetime.datetime.now()
        for h in View.horario_listar():
            if h.get_data()>= agora and h.get_confirmado() == False and h.get_id_cliente() == None and h.get_id_profissional() == id_profissional:
                r.append(h)
            r.sort(key = lambda h : h.get_data())
        return r

    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key = lambda obj : obj.get_nome())
        return r
    def profissional_inserir(nome, email, especialidade, conselho, senha):
        if email == 'admin': raise ValueError('E-mail já cadastrado')
        for obj in View.cliente_listar():
            if obj.get_email() == email: raise ValueError('Email já cadastrado')
        for obj in View.profissional_listar():
            if obj.get_email() == email: raise ValueError('Email já cadastrado')
        profissional = Profissional(0, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.inserir(profissional)
    def profissional_atualizar(id, nome, email, especialidade, conselho, senha):
        if email == 'admin': raise ValueError('E-mail já cadastrado')
        for obj in View.cliente_listar():
            if obj.get_email() == email: raise ValueError('Email já cadastrado')
        for obj in View.profissional_listar():
            if obj.get_id() != id and obj.get_email() == email: raise ValueError('Email já cadastrado')
        profissional = Profissional(id, nome, email, especialidade, conselho, senha)
        ProfissionalDAO.atualizar(profissional)
    def profissional_excluir(id):
        for obj in View.horario_listar():
            if obj.get_id_profissional() == id: raise ValueError('Profissional com horário cadastrado, não é possível excluir')
        profissional = Profissional(id, 'sem nome', 'sem email', 'sem especialidade', 'sem conselho', 'sem senha')
        ProfissionalDAO.excluir(profissional)
    def profissional_listar_id(id):
        profissional = ProfissionalDAO.listar_id(id)
        return profissional
    def horario_filtrar_profissional(id_profissional):
        r= []
        for h in View.horario_listar():
            if h.get_id_profissional() == id_profissional:r.append(h) 
        return r
    def horario_filtrar_cliente(id_cliente):
        r = []
        for h in View.horario_listar():
            if h.get_id_cliente() == id_cliente: r.append(h)
        return r
    def profissional_inserir_agenda(id, dia, hora_inicio, hora_final, intervalo):
        h = datetime.datetime.combine(dia, hora_inicio)
        fim = datetime.datetime.combine(dia, hora_final)
        intervalo_td = datetime.timedelta(minutes=int(intervalo))
        while h <= fim:
            View.horario_inserir(h, False, None, None, id)
            h += intervalo_td