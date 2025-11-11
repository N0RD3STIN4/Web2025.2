import streamlit as st
import time
from views import View
import pandas as pd


class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profs = View.profissional_listar()
        if len(profs) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profs)
            horarios = View.horario_agendar_horario(profissional.get_id())
            if len(horarios) == 0:
                st.write("Nenhum horário disponível")
            else:
                horario = st.selectbox("Informe o horário", horarios)
                servicos = View.servico_listar()
                servico = st.selectbox("Informe o serviço", servicos)
                if st.button("Agendar"):
                    View.horario_atualizar(
                        horario.get_id(),
                        horario.get_data(),
                        False,
                        st.session_state["usuario_id"],
                        servico.get_id(),
                        profissional.get_id(),
                    )
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()


class MeusServicosUI:
    def main():
        st.header("Meus Serviços")
        horarios = View.horario_filtrar_cliente(st.session_state["usuario_id"])
        if len(horarios) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            list_dict = []
            for obj in horarios:
                list_dict.append(obj.to_json())
            df = pd.DataFrame(list_dict)
            if "id_cliente" in df.columns:
                df = df.drop(columns=["id_cliente"])
            st.dataframe(df)
