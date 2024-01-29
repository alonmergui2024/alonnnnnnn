import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
import random
import json
import os

URL = "https://www.espn.com/nba/teams"
header = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}
response = requests.get(URL, headers=header)
s = BeautifulSoup(response.content, "html.parser")
results = s.find(id="fitt-analytics")


class Autocomplete:
    def __init__(self, team):
        self.team = team

    def suggest(self, prefix):
        prefix = prefix.lower()
        suggestions = []
        for word in self.team:
            for miniword in word.split(" "):
                if miniword.lower().startswith(prefix.lower()) or miniword.lower() == prefix.lower():
                    suggestions.append(word)
                    break

        return suggestions


if results:
    team = []
    team.append("None")
    teams = results.find_all('h2', class_='di clr-gray-01 h5')
    for i in teams:
        team.append(i.text)
    autocomplete_engine = Autocomplete(team)


check = False

data = []
a = False


st.set_page_config(
    page_title="Basketball",
    page_icon=r":basketball:",

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
                    st.success(f"Welcome, {username}! favorite team: {fav_team}")
                st.session_state.runpage = main
                st.experimental_rerun()
            else:
                st.warning("Incorrect password. Please check for spelling and try again.")
    else:
        st.warning("User does not exist. Please sign up or check the username.")


def homepage():
    st.title("BasketBall - Team Information")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    def Login():
        col1.title("Login")
        if col6.button("Signup",on_click=click_button):
            username = st.text_input("Enter your username:")
            password = st.text_input("Enter your password:", type="password")
            fav_team = st.selectbox('Enter your favorite team (optional): ',(team))
            if st.button("Sign Up"):
                sign_up(username, password, fav_team)
                return username,password,fav_team
        
        st.table()
        if st.button("Login",on_click=click_button):
            if Login(username, password):
                with open(json_file_path, "r") as file:
                    users = json.load(file)
                    user_data = users.get(username)
                    fav_team = user_data.get("fav_team")
                return username, password, fav_team
    Login()
            
        


            

def main():
    def Account():
        selected2 = option_menu(None, ["Account", "this week games", "all sesson games"], 
            icons=['house', 'celender', '🌎'], 
            menu_icon="cast", default_index=0, orientation="horizontal")
        st.title(selected2)
        if selected2 == "Home":
            st.text("Username:")
            st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>{username}</div>", unsafe_allow_html=True)
            st.text("Password")
            st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>{password}</div>", unsafe_allow_html=True, type="password")
            st.text("Favorite team")
            st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>{fav_team}</div>", unsafe_allow_html=True)

            if st.button("Edit Information"):
                st.text("Enter new username:")
                username = st.text_input()
                st.text("Enter new password:")
                password = st.text_input( type="password")
                st.text("Enter new favorite team:")
                fav_team = st.selectbox('Enter your favorite team (optional): ',(team))

            if st.button("Confirm Changes"):
                st.text("Username:")
                st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>{username}</div>", unsafe_allow_html=True)
                st.text("Password")
                st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>{password}</div>", unsafe_allow_html=True, type="password")
                st.text("Favorite team")
                st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 5px;'>{fav_team}</div>", unsafe_allow_html=True)
                st.success("Information updated successfully!")
            print(inf)


    Account()


inf = homepage()
