from basketball_data import Basketball
import streamlit as st
import pandas as pd

def this_week():
    game = Basketball()
    team = st.selectbox("select a team: ", game.get_teamlist())
    week = ""
    games = {
        "home": [],
        "away": [],
        "time": []
    }
    if team == "None":
        week = game.this_week()
    else:
        week = game.this_week_team(team)
    for item in week:
        games["home"].append(item[0])
        games["away"].append(item[1])
        games["time"].append(item[2])
    
    df = pd.DataFrame(games)
    st.table(df)
