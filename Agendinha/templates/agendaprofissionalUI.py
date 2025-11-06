import streamlit as st
from views import View
from datetime import datetime, timedelta
import time
import pandas as pd

class AbrirAgenda:
    def main():
        st.header('Abrir Minha Agenda')
        dia = st.date_input("Data")
        hora_inicial = st.time_input("Hora inicial")
        hora_final = st.time_input("Hora final")
        intervalo = st.number_input("Intervalo (min)", min_value=0, step=5)
        if st.button('Abrir Agenda'):
            try:
                View.profissional_inserir_agenda(st.session_state["usuario_id"], dia, hora_inicial, hora_final, intervalo)
                st.success('Horários inseridos com sucesso')
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
            
class MinhaAgenda:
    def main():
        st.header('Minha Agenda')
        horarios = View.horario_filtrar_profissional(st.session_state['usuario_id'])
        agora = datetime.now()
        if len(horarios) == 0: st.write('Nenhum horário')
        else:
            list_dict = []
            for obj in horarios:
                if obj.get_data() >= agora:
                    list_dict.append(obj.to_json())
            df = pd.DataFrame(list_dict)
            if "id_profissional" in df.columns:
                df = df.drop(columns=["id_profissional"])
            st.dataframe(df)
            
class ConfirmarServicoUI:
    def main():
        st.header('Confirmar Serviço')
        horarios = View.horario_filtrar_profissional(st.session_state['usuario_id'])
        horarios_filtrados = []
        if len(horarios) == 0: st.write('Nenhum horário cadastrado')
        for obj in horarios:
            if obj.get_id_cliente() != None and obj.get_confirmado() == False: horarios_filtrados.append(obj)
        if len(horarios_filtrados) == 0: st.write('Nenhum horário a confirmar')
        else: 
            horario = st.selectbox('Informe o horário', horarios_filtrados, index=None)
            # cliente = st.selectbox('Cliente', horario.get_id_cliente(), index=None)
            if st.button('Confirmar'):
                View.horario_atualizar(horario.get_id(), horario.get_data(), True, horario.get_id_cliente(), horario.get_id_servico(), horario.get_id_profissional())
                st.success('Horario confirmado com sucesso')
                time.sleep(2)
                st.rerun()