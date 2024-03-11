import streamlit as st
from register import Login, sign_up, info

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True



def homepage():
    st.title("User Authentication System")
    page = st.sidebar.radio("Navigation", ["Sign Up","Change info", "Login"])


    if page == "Sign Up":
        st.header("Sign Up")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        fav_team = st.text_input("Choose your favorite team:")
        st.button('Sign up', on_click=click_button)
        if st.session_state.clicked:
            sign_up(username, password, fav_team)

    elif page == "Change info":
        st.header("Change info")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        st.button('Change info', on_click=click_button)
        if st.session_state.clicked:
            if Login(username, password):
                pass
            
    else:
        st.header("Login")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        st.button('Login', on_click=click_button)
        if st.session_state.clicked:
            if info(username, password):
                pass
