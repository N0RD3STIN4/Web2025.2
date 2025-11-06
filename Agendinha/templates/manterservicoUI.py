import streamlit as st
import pandas as pd
import time
from views import View

class ManterServicoUI:
    def main():
        st.header('Cadastro de Serviçõs')
        tab1, tab2, tab3, tab4, = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()
    
    def listar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            list_dic = [] 
            for obj in servicos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        desc = st.text_area('Informe a descrição')
        valor = st.number_input('Informe o valor')
        if st.button('Inserir'):
            try:
                servico = View.servico_inserir(desc, valor)
                st.success('Serviço inserido com sucesso')
                st.write(servico)
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Atualização de serviços', servicos)
            desc = st.text_input('Novo desc', op.get_descricao())
            valor = st.number_input('Novo valor', op.get_valor())
            if st.button('Atualizar'):
                try:
                    id = op.get_id()
                    View.servico_atualizar(id, desc, valor)
                    st.success('Serviço atualizado com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()

    def excluir():
        servicos = View.servico_listar()
        if len(servicos) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Exclusão de serviços', servicos)
            if st.button('Excluir'):
                try:
                    id = op.get_id()
                    View.servico_excluir(id)
                    st.success('Serviço excluído com sucesso')
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()