import streamlit as st
from homepage import homepage   
from this_week import this_week
from welcome import welcome_page

json_file_path = "users.json"

st.set_page_config(
    page_title="Basketball",
    page_icon=r":basketball:",

)


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

page = st.sidebar.selectbox("Page", ["account", "this week", "welcome"])
if page == "account":
    homepage()
elif page == "this week":
    this_week()
if page == "welcome":
    welcome_page()