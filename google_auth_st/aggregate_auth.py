import streamlit as st
from .google_auth import get_logged_in_user_email, show_login_button

def add_auth(
    login_button_text: str = "Login with Google",
    login_button_color: str = "#3383FF",
    login_sidebar: bool = True,
):
    user_email = get_logged_in_user_email()

    if not user_email:
        show_login_button(
            text=login_button_text, color=login_button_color, sidebar=login_sidebar
        )
        st.stop()

    if st.sidebar.button("Logout", type="primary"):
        del st.session_state.email
        st.rerun()

