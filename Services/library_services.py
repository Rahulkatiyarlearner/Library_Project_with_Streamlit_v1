from data.library_database import library_database
from data.member_database import member_database
import re
from datetime import date 
import pandas as pd

class library_services:

    @staticmethod
    def validation_entry(in_book_name,in_ISBN):
        ISBN_pattern = r"^\d{13}$"
        if len(in_book_name.strip()) == 0:
            return "Book Name not Provided"
        elif len(in_ISBN) != 13 or not re.match(ISBN_pattern,in_ISBN):
            return "ISBN not provide in Correct Format"
        else:
            ld = library_database()
            get_max_serial = ld.get_max_serial_number()
            if get_max_serial is None or get_max_serial[0] is None:
                get_max_serial = 10000000
            else:
                get_max_serial = get_max_serial[0] + 1
                ld.enter_book(get_max_serial,in_book_name,in_ISBN,'','')
                ret_data = "Book added in Library. Book id is - " + str(get_max_serial)
                return ret_data


    @staticmethod
    def ret_bk_list():
        ld = library_database()
        bk_list = ld.load_books()
        return_list = [bk[0] for bk in bk_list]
        return return_list

    @staticmethod
    def validate_member_id(in_id,in_book_name):
        ID_pattern = r"^\d{8}$"
        if len(in_id) != 8 or not re.match(ID_pattern,in_id):
            return "Please enter data correctly"
        else:
            mb = member_database()
            out_name = mb.chk_id(in_id)
            if out_name is None:
                return "User id not present"
            else:
                ld = library_database()
                ld.update_issuer(in_id,in_book_name)
                rtrn_data = "Book : "+in_book_name + " has now been issued to " + out_name[0] + "."
                return rtrn_data

    @staticmethod
    def get_book_list(in_id):
        ld = library_database()
        bk_list = ld.issue_books_usr(in_id)
        if len(bk_list) != 0 :
            new_list = [list[0] for list in bk_list]
            return new_list
        else:
            return "None"


    @staticmethod
    def ret_bk_clc_fine(in_id):
        ld = library_database()
        bk_list = ld.issue_books_usr(in_id)
        if len(bk_list) != 0 :
            new_list = []
            for bk in bk_list:
                fine = 14 + (((date.fromisoformat(bk[2]) - date.today()).days))
                if fine < 0:
                    new_list.append(f"{bk[0]} - {bk[1]} | Fine : {fine}")
                else:
                    new_list.append(f"{bk[0]} - {bk[1]} | Fine : 0")
            return new_list
        else:
            return "None"


    @staticmethod
    def book_return_fine_calc(list_book):
        ld = library_database()
        Total_fine = 0
        for list_data in list_book:
            get_date = ld.get_date(list_data)
            day_diff = (((date.fromisoformat(get_date[0]) - date.today()).days)*-1)
            if day_diff > 14 :
                Total_fine = Total_fine + (day_diff - 14)
            ld.remove_issuer(list_data)
        return Total_fine 

    @staticmethod
    def get_lib_all_data():
        ld = library_database()
        data = ld.get_all_date()
        column_data = ["SERIAL_NUMBER","BOOK_NAME","ISBN_NUMBER","ISSUE_DATE","LIBRARY_ID"]
        df = pd.DataFrame(data,columns=column_data)
        return df

    








# ls = library_services()
# ls.get_lib_all_data()
# ls.book_return_fine_calc(["Ancient Star: The Art of Beginning Again","Curious Horizon: A Guide to New Horizons"])
# print(ls.get_book_list(10000004))
# print(ls.validate_member_id("10000002","Secret Ocean: A Journey Beyond Time"))






        



