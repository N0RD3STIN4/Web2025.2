from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissional import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.agendaclienteUI import AgendarServicoUI, MeusServicosUI
from templates.agendaprofissionalUI import AbrirAgenda, MinhaAgenda, ConfirmarServicoUI
from templates.perfiladminUI import PerfilAdminUI
from views import View
import streamlit as st
class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes",
            "Cadastro de Serviços","Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": PerfilAdminUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar como Cliente", "Entrar como Profissional",
        "Abrir Conta"])
        if op == "Entrar como Cliente": LoginUI.cliente()
        if op == "Entrar como Profissional": LoginUI.profissional()
        if op == "Abrir Conta": AbrirContaUI.main()
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Meus Serviços": MeusServicosUI.main()
    def menu_profissional():    
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Agenda", "Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Agenda": AbrirAgenda.main()
        if op == "Minha Agenda": MinhaAgenda.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            else: 
                if st.session_state["usuario_tipo"] == "c": IndexUI.menu_cliente()
                elif st.session_state["usuario_tipo"] == "p": IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()
    def main():
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()
IndexUI.main() 