import streamlit as st
from homepage import homepage   
from this_week import this_week

json_file_path = "users.json"

st.set_page_config(
    page_title="Basketball",
    page_icon=r":basketball:",

)


if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

page = st.sidebar.selectbox("Page", ["homepage", "this week"])
if page == "homepage":
    homepage()
elif page == "this week":
    this_week()