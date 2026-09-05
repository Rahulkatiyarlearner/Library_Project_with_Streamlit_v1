import streamlit as st 
from Services.member_services import member_services
from Services.library_services import library_services




def main_Screen():

    st.set_page_config(
    layout="wide",
    page_title="Main Page"
    )

    if "logout_pg" in st.session_state.keys():
        if st.session_state["logout_pg"] == True:
            st.session_state["authenticated"] = False
            st.rerun()

    st.title("ABC Library",text_alignment="center")


    st.subheader("Main Page",text_alignment="center")


    cols1 , cols2 , cols3, cols4, cols5 = st.columns([3,2,12,2,2])


    with cols1:
        st.button("Add Member",width=250,key="add_member")
        st.button("Add Book",width=250,key="add_books")
        st.button("Issue Book",width=250,key="iss_books")
        st.button("Return Book",width=250,key="ret_books")
        st.button("Search Book",width=250,key="src_books")
        st.button("Check Currently Issued Book",width=250,key="cib_books")

    with cols3:

        #Add Member
        if "submit_add_member" in st.session_state:
            if st.session_state["submit_add_member"] == True:
                out = member_services.validation(st.session_state["member_added"])
                st.success(out)
            else:
                st.error("Name not Provided in Add Member")

        #Add Book
        if "add_libbook" in st.session_state:
            if st.session_state["add_libbook"] == True:
                out = library_services.validation_entry(st.session_state["book_name"],st.session_state["book_isbn"])
                st.success(out)
            else:
                st.error("Data not added Properly in Add Book")


        #Issue Book
        if "iss_libbook" in st.session_state:
            if st.session_state["iss_libbook"] == True:
                out = library_services.validate_member_id(st.session_state["iss_member_id"],st.session_state["iss_book_name"])
                st.success(out)
            else:
                st.error("Data not provide in Issue Book")


        #Return Books
        if "ret_libbook" in st.session_state:
            if st.session_state["ret_libbook"] == True:
                bk_list = library_services.get_book_list(st.session_state["ret_mem_id"])
                if bk_list == "None":
                    st.success(f"No book alloated to {st.session_state["ret_mem_id"]}")
                else:
                    usr_name = member_services.get_usr_name(st.session_state["ret_mem_id"])
                    st.subheader("Return Book")
                    st.write(f"Member ID : {st.session_state["ret_mem_id"]}")
                    st.write(f"Member Name : {usr_name}")
                    
                    with st.form("add_books_form"):
                        st.multiselect(
                        "Select Books you want to Return:",
                        bk_list,
                        key="books_slt"
                        )
                        st.form_submit_button("Return books",key="rtrn_bks")

        if "rtrn_bks" in st.session_state:
            if st.session_state["rtrn_bks"] == True:
                out_ret = library_services.book_return_fine_calc(st.session_state["books_slt"])
                st.success("Books returned.")
                if out_ret > 0:
                    st.write(f"Total Fine - {out_ret}")
                



        #-------------Display Section-----------#

        if st.session_state["add_member"] == True:
            st.subheader("Add Member")
            with st.form("add_member_form"):
                st.text_input("Please Enter the Member Name",max_chars=36,placeholder="Type Here...",
                                                            key="member_added")
                st.form_submit_button("Add Member",key="submit_add_member")
        

        if st.session_state["add_books"] == True:
            st.subheader("Add Book")
            with st.form("add_books_form"):
                st.text_input("Please Enter Book Name       ",max_chars=100,placeholder="Type Here...",
                                                            key="book_name")
                st.text_input("Please Enter Book ISBN number",max_chars=13,placeholder="Type Here...",
                                                            key="book_isbn")
                st.form_submit_button("Add Book",key="add_libbook")


        
        if st.session_state["iss_books"] == True:
            st.subheader("Issue Book")
            book_list = library_services.ret_bk_list()
            with st.form("iss_books_form"):
                st.text_input("Please Enter Member ID       ",max_chars=8,placeholder="Type Here...",
                                                            key="iss_member_id")
                st.selectbox("Select the book               ",book_list,index=None,
                                                            placeholder="Type to search for a book...",
                                                            key="iss_book_name")
                st.form_submit_button("Issue Book",key="iss_libbook")


        if st.session_state["ret_books"] == True:
            st.subheader("Return Book")
            mem_list = member_services.ret_usr_list()
            with st.form("ret_books_form"):
                st.selectbox("Select the Member ID            ",mem_list,index=None,
                                                            placeholder="Type to search for a Member ID...",
                                                            key="ret_mem_id")
                st.form_submit_button("Get book list",key="ret_libbook")
        

        if st.session_state["src_books"] == True:
            st.subheader("Search Books")
            book_list = library_services.ret_bk_list()
            st.selectbox("Select the book               ",book_list,index=None,
                                                        placeholder="Type to search for a book...",
                                                        key="iss_book_name")


        if st.session_state["cib_books"] == True:
            st.subheader("Currently Issued Books")
            lib_df = library_services.get_lib_all_data()
            st.dataframe(lib_df,width=1500,height=300)


    with cols5:
        st.button("Logout",key="logout_pg")








        







