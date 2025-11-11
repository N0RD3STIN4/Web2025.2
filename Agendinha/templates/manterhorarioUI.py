import streamlit as st
import pandas as pd
import time
from views import View
from datetime import datetime


class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterHorarioUI.listar()
        with tab2:
            ManterHorarioUI.inserir()
        with tab3:
            ManterHorarioUI.atualizar()
        with tab4:
            ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            list_dic = []
            for obj in horarios:
                cliente = View.cliente_listar_id(obj.get_id_cliente())
                servico = View.servico_listar_id(obj.get_id_servico())
                profissional = View.profissional_listar_id(obj.get_id_profissional())
                if cliente != None:
                    cliente = cliente.get_nome()
                if servico != None:
                    servico = servico.get_descricao()
                if profissional != None:
                    profissional = profissional.get_nome()
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()
        data = st.text_input(
            "Informe a data e o horário do serviço",
            datetime.now().strftime("%d/%m/%Y %H:%M"),
        )
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index=None)
        servico = st.selectbox("Informe o serviço", servicos, index=None)
        profissional = st.selectbox("Informe o profissional", profissionais, index=None)
        if st.button("Inserir"):
            try:
                if cliente != None:
                    cliente = cliente.get_id()
                if servico != None:
                    servico = servico.get_id()
                if profissional != None:
                    profissional = profissional.get_id()
                View.horario_inserir(
                    datetime.strptime(data, "%d/%m/%Y %H:%M"),
                    confirmado,
                    cliente,
                    servico,
                    profissional,
                )
                st.success("Horário inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            clientes = View.cliente_listar()
            servicos = View.servico_listar()
            profissionais = View.profissional_listar()
            op = st.selectbox("Atualização de horários", horarios)
            data = st.text_input(
                "Informe a nova data e horário do serviço",
                datetime.now().strftime("%d/%m/%Y %H:%M"),
            )
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente = (
                None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            )
            id_servico = (
                None if op.get_id_servico() in [0, None] else op.get_id_servico()
            )
            id_profissional = (
                None
                if op.get_id_profissional() in [0, None]
                else op.get_id_profissional()
            )
            cliente = st.selectbox(
                "Informe o novo cliente",
                clientes,
                next(
                    (i for i, c in enumerate(clientes) if c.get_id() == id_cliente),
                    None,
                ),
            )
            servico = st.selectbox(
                "Informe o novo servico",
                servicos,
                next(
                    (i for i, s in enumerate(servicos) if s.get_id() == id_servico),
                    None,
                ),
            )
            profissional = st.selectbox(
                "Informe o novo profissional",
                profissionais,
                next(
                    (
                        i
                        for i, s in enumerate(profissionais)
                        if s.get_id() == id_profissional
                    ),
                    None,
                ),
            )
            if st.button("Atualizar"):
                try:
                    id_cliente = None
                    id_servico = None
                    if cliente != None:
                        cliente = cliente.get_id()
                    if servico != None:
                        servico = servico.get_id()
                    if profissional != None:
                        profissional = profissional.get_id()
                    View.horario_atualizar(
                        op.get_id(),
                        datetime.strptime(data, "%d/%m/%Y %H:%M"),
                        confirmado,
                        cliente,
                        servico,
                        profissional,
                    )
                    st.success("Horário atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de horarios", horarios)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.horario_excluir(id)
                    st.success("Horário excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
