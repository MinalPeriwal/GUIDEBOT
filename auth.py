import streamlit as st
from database import create_user, authenticate_user

def show_login_page():
    """Display login/register interface"""
    st.title("🤖 GUIDEBOT")
    st.subheader("Welcome! Please login or register to continue.")
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
            
            if login_button:
                if authenticate_user(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
    
    with tab2:
        with st.form("register_form"):
            new_username = st.text_input("Choose Username")
            new_email = st.text_input("Email")
            new_password = st.text_input("Choose Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            register_button = st.form_submit_button("Register")
            
            if register_button:
                if new_password != confirm_password:
                    st.error("Passwords don't match")
                elif len(new_password) < 6:
                    st.error("Password must be at least 6 characters")
                elif create_user(new_username, new_email, new_password):
                    st.success("Account created successfully! Please login.")
                else:
                    st.error("Username or email already exists")

def logout():
    """Handle user logout"""
    st.session_state.authenticated = False
    st.session_state.username = None
    if 'messages' in st.session_state:
        del st.session_state.messages
    st.rerun()