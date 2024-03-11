import json
import os
import streamlit as st
import pandas as pd


json_file_path = "users.json"




if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


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
        st.warning("Username is already taken. Please choose another one")
    elif username=="":
        st.warning("You have to enter a username")
    elif password=="":
        st.warning("You have to enter a password")
    else:
        user_data = {"password": password}
        birthday =""
        users[username] = user_data
        users[f"{username}_info"] = {'birthday':birthday,'fav_team':fav_team}
        with open(json_file_path, "w") as file:
            json.dump(users, file)
        st.success("You have successfully signed up!")







def Login(username, password):
    if user_exists(username):
        with open(json_file_path, "r") as file:
            users = json.load(file)
            user_data = users.get(username)
            if user_data and user_data.get("password") == password:
                fav_team = user_data.get("fav_team")
                st.success(f"Welcome, {username}! favorite team: {fav_team}")
                return True
            else:
                st.warning("Incorrect password. Please check for spelling and try again.")
    else:
        st.warning("User does not exist. Please sign up or check the username.")




def info(username, password):
    users = {}
    if user_exists(username):
        with open(json_file_path, "r") as file:
            users = json.load(file)
            user_data = users.get(username)    
            if user_data and user_data.get("password") == password:
                additional_info = users.get(f"{username}_info")
               


                st.markdown("---")
                st.subheader("👤 " + "User Information")
               
                st.write(f"**Username:** {username} 👩‍💻")
                st.write(f"**birthday:** {additional_info.get('Age', 'N/A')} 🎂")
                st.write(f"**favorite team:** {additional_info.get('fav_team', 'N/A')} 🌆")
                return True
            else:
                st.error("❌ " + "Incorrect password. Please try again.")
    else:
        st.error("❌ " + "User does not exist. Please sign up or check the username.")



