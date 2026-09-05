from data.database_manager import database_manager

class member_database:

    def __init__(self):
        self.db = database_manager("Library_member.db")

    def create_tbl(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Library_Member_Table(
            LIBRARY_ID  BIGINT NOT NULL PRIMARY KEY,
            MEMBER_NAME FULL_NAME CHAR(36) NOT NULL 
            )
            """
            )

    def delete_tbl(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS Library_Member_Table")


    def enter_member(self,lib_id,lib_mem):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO Library_Member_Table
            (LIBRARY_ID,MEMBER_NAME) VALUES (?,?)""",
            (lib_id,lib_mem)
            )


    def chk_max_id(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT MAX(LIBRARY_ID)
            FROM Library_Member_Table
            """
            ) 
            return cursor.fetchone()
    
    def chk_id(self,in_id):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT MEMBER_NAME
            FROM Library_Member_Table
            WHERE LIBRARY_ID = ?
            """,
            (in_id,)
            ) 
            return cursor.fetchone()


    def chk_usr(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
            """
            SELECT MAX(LIBRARY_ID)
            FROM Library_Member_Table"""
            ) 
            return cursor.fetchone()


    def load_users(self):
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            SELECT LIBRARY_ID FROM Library_Member_Table 
            ORDER BY LIBRARY_ID ASC
            """
            )
            return cursor.fetchall()



            
















