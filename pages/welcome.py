import streamlit as st
def welcome_page():
    st.title(":basketball: Welcome to Basketball Stats Web App")
    st.write("""
    This web app allows you to explore basketball statistics, analyze player performances,
    and gain insights into various aspects of the game.
    
    Choose an option from the sidebar to get started!
    """)

    st.subheader(("📚 Available Pages:"))

    st.markdown(f"- **{('User Entrance Field')}**: {('Navigate to the user entrance field to sign up, sign in, or change user information.')}")
    st.markdown(f"- **{('Stock Analysis')}**:  {('Explore the Stock Analysis page to analyze stock prices, make predictions, and check investment opportunities.')}")
    st.markdown(f"- **{('Choose Language')}**:  {('If you prefer a different language, use this page to choose your preferred language.')}")

    st.write((
        "Feel free to explore the different functionalities and make the most out of the Stock Analyzer App! 📊📈"
    ))
    def MarkDownCode(file_path,file_name):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

            with st.expander(file_name):
                st.text(text)
        except UnicodeDecodeError:
            st.error(f"Unable to decode the content of the file: {file_path}")

    