import streamlit as st
from UI.login_screen import login_screen
from UI.main_screen import main_Screen

def main():

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"] != True :
        login_screen()
    else:
        main_Screen()


if __name__ == "__main__":
    main()