import streamlit as st
import time


def login_screen():

    st.set_page_config(
    layout="centered",
    page_title="Login Page"
    )   

    st.title("ABC Library")
    st.subheader("Please Login Here")

    st.write("-- Use Username = admin || Password = 1234 --")

    if "login_dtls" in st.session_state:
        if st.session_state["login_dtls"] == True:
            if st.session_state["User_Name"]== "admin" and st.session_state["User_Pass"] == "1234":
                st.success("Login Success")
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Login Failed - Enter correct data")

    if st.session_state["authenticated"] == False:
        with st.form("add_member_form"):
            st.text_input("Username",max_chars=5,placeholder="Type Here...",key="User_Name")
            st.text_input("Password",max_chars=4,placeholder="Type Here...",key="User_Pass")
            st.form_submit_button("Login",key="login_dtls")




