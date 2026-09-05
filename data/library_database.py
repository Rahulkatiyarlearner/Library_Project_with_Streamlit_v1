from data.database_manager import database_manager
from datetime import date

class library_database:

    def __init__(self):
        self.db = database_manager("Library_books.db")

    def create_tbl(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Library_books_Table(
            SERIAL_NUMBER  BIGINT NOT NULL PRIMARY KEY,
            BOOK_NAME CHAR(100) NOT NULL,
            ISBN_NUMBER CHAR(13) NOT NULL,
            ISSUE_DATE DATE,
            LIBRARY_ID  BIGINT, 

            FOREIGN KEY (LIBRARY_ID) REFERENCES Library_Member_Table(LIBRARY_ID)
            )
            """
            )

    def delete_tbl(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS Library_books_Table")


    def enter_book(self,serial_num,book_name,isbn,in_date,in_id):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO Library_books_Table
            (SERIAL_NUMBER,BOOK_NAME,ISBN_NUMBER,ISSUE_DATE,LIBRARY_ID) VALUES (?,?,?,?,?)""",
            (serial_num,book_name,isbn,in_date,in_id)
            )

    def get_max_serial_number(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT MAX(SERIAL_NUMBER) 
            FROM Library_books_Table
            """
            )
            return cursor.fetchone()

    
    def load_books(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT BOOK_NAME FROM Library_books_Table 
            ORDER BY BOOK_NAME ASC
            """
            )
            return cursor.fetchall()

    def update_issuer(self,in_id,in_book_name):
         with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE Library_books_Table
            SET ISSUE_DATE = ?,
                LIBRARY_ID = ?
            WHERE BOOK_NAME = ?
            """,(date.today(),in_id,in_book_name)
            )


    def issue_books_usr(self,in_id):
         with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT BOOK_NAME
            FROM Library_books_Table
            WHERE LIBRARY_ID = ?
            """,(in_id,)
            )
            return cursor.fetchall()

            

    def get_date(self,bk_name):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT ISSUE_DATE
            FROM Library_books_Table
            WHERE BOOK_NAME = ?
            """,(bk_name,)
            )
            return cursor.fetchone()


    def remove_issuer(self,in_book_name):
         with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE Library_books_Table
            SET ISSUE_DATE = '',
                LIBRARY_ID = ''
            WHERE BOOK_NAME = ?
            """,(in_book_name,)
            )


    def get_all_date(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT SERIAL_NUMBER,BOOK_NAME,ISBN_NUMBER,ISSUE_DATE,LIBRARY_ID
            FROM Library_books_Table
            WHERE LIBRARY_ID != ''
            """
            )
            return cursor.fetchall()





