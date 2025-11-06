from views import View
import streamlit as st
import time

class PerfilAdminUI:
    def main():
        st.header('Alterar Senha')
        op = View.cliente_listar_id(st.session_state['usuario_id'])
        senha = st.text_input('Informe a nova senha', op.get_senha(), type="password")
        if st.button('Atualizar'):
            View.cliente_atualizar(op.get_id(), op.get_nome(), op.get_email(), op.get_fone(), senha)
            st.success('Senha atualizada com sucesso')
            time.sleep(2)
            st.rerun()