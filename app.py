import streamlit as st
import requests
import pandas as pd
import time
import datetime
from streamlit_extras.switch_page_button import switch_page
import random
import json
import os

check = False

data = []
a = False


st.set_page_config(
    page_title="Stocks analyzer",
    page_icon=r"icons8-stock-48.png",

)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True



json_file_path = "users.json"



def user_exists(username):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            file_contents = file.read()
            if file_contents:
                try:
                    users = json.loads(file_contents)
                except json.JSONDecodeError:
                    st.error("Error decoding JSON. Please check the file format.")
                    return False
            else:
                users = {}
                with open(json_file_path, "w") as empty_file:
                    json.dump(users, empty_file)
    else:
        users = {}
    return username in users


def sign_up(username, password, fav_team):
    if os.path.exists(json_file_path):
        with open(json_file_path, "r") as file:
            file_contents = file.read()
            if file_contents:
                try:
                    users = json.loads(file_contents)
                except json.JSONDecodeError:
                    st.error("Error decoding JSON. Please check the file format.")
                    return
            else:
                users = {}
    else:
        users = {}

    if username in users:
        st.warning("Username is already taken. Please choose another one.")
    else:
        user_data = {"password": password, "fav_team": fav_team}
        users[username] = user_data
        with open(json_file_path, "w") as file:
            json.dump(users, file)
        st.session_state.runpage = main
        st.experimental_rerun()





# Function to sign in a user
def Login(username, password):
    if user_exists(username):
        with open(json_file_path, "r") as file:
            users = json.load(file)
            user_data = users.get(username)
            if user_data and user_data.get("password") == password:
                fav_team = user_data.get("fav_team")
                if fav_team:
                    st.success(f"Welcome, {username}! favorite team: {fav_team}")
                else:
                    fav_team = "None"
                    st.success(f"Welcome, {username}!")
                st.session_state.runpage = main
                st.experimental_rerun()
            else:
                st.warning("Incorrect password. Please check for spelling and try again.")
    else:
        st.warning("User does not exist. Please sign up or check the username.")


def homepage():
    st.title("BasketBall - Team Information")

    page = st.sidebar.radio("Navigation", ["Sign Up", "Login"])

    if page == "Sign Up":
        st.header("Sign Up")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        fav_team = st.text_input("Enter your favorite team (optional):")
        if st.button("Sign Up"):
            sign_up(username, password, fav_team)
            return username,password,fav_team
        

    elif page == "Login":
        st.header("Login")
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type="password")
        if st.button("Login"):
            if Login(username, password):
                with open(json_file_path, "r") as file:
                    users = json.load(file)
                    user_data = users.get(username)
                    fav_team = user_data.get("fav_team")
                return username, password, fav_team

            

def main():
    def Account():
        st.chat_message("hi")
    page = st.sidebar.radio("Select Page", ["Account", "Information", "real time stock investment"])
    if page == "Account":
        Account()
    elif page == "Information":
        pass
    elif page == "real time stock investment":
        pass

if 'runpage' not in st.session_state:
    st.session_state.runpage = homepage

st.session_state.runpage()
