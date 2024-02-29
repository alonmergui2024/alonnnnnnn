import basketball_data
import streamlit as st
import json

st.set_page_config(
    page_title="Basketball",
    page_icon=r":basketball:",

)

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