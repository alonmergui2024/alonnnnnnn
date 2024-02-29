import streamlit as st
import json
from register import Login, sign_up, user_exists

json_file_path = "users.json"

st.set_page_config(
    page_title="Basketball",
    page_icon=r":basketball:",

)
a = False

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

username = ""
def main():
    default_options = ["Sign Up", "Login"]
    options = default_options

    page = st.sidebar.selectbox("Navigation", options)
    if page == "Sign Up":
        st.header("Sign Up")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        fav_team = st.selectbox('Enter your favorite team (optional): ',("none"))
        
        st.button('Sign up', on_click=click_button)
        if st.session_state.clicked:
            sign_up(username, password,fav_team)

                

    elif page == "Login":
        st.header("Login")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        st.button('Login', on_click=click_button)
        if st.session_state.clicked:
            if Login(username, password):
                with open(json_file_path, "r") as file:
                    users = json.load(file)
                    user_data = users.get(username)
                    fav_team = user_data.get("fav_team")
                

