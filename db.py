import sqlite3
from sqlite3 import Error

class sqlite_crud:

    def __init__(self, db_name, table_name, schema):
        self.db_name = db_name
        self.table_name = table_name
        self.con = None
        self.cur = None
        self.schema = schema # schema must be dict
        self.pID = 0

    def create_connection(self):
        try:
            self.con = sqlite3.connect(self.db_name)
            self.cur = self.con.cursor()
        except Error as e:
            print(e)

    def create_table(self):
        try:
            query = "CREATE TABLE " + self.table_name + " (" + ','.join(self.schema) + ");"
            self.cur.execute(query)
        except Error as e:
            print(e)

    def insert_data(self, data):
        # data must be list 
        query_assist = ",".join([ "?" for _ in range(len(data))])
        query = "INSERT INTO "+ self.table_name + "(" + ','.join(self.schema) + ") VALUES(" + query_assist + ");"
        self.cur.execute(query, data)
        self.con.commit()
        self.pID = self.cur.lastrowid
        return self.pID

    def update_data(self, data ):
        # query_assist = ",".join([ "?" for _ in range(len(data))])
        update_col = ""
        update_value = ""
        condition = "id = 1"
        query1 = "UPDATE "+ self.table_name + " SET "+ update_col +"="+ update_value +"WHERE "
        query = """UPDATE employees SET name=Kamal WHERE id=1"""
        self.cur.execute(query)
        self.con.commit()

    def view_data(self):
        self.cur.execute("SELECT * FROM "+ self.table_name)
        rows = self.cur.fetchall()

        for row in rows:
            print(row)

    def delete_task(self, id):
        sql = 'DELETE FROM '+ self.table_name + 'WHERE id=?'
        self.cur.execute(sql, (id,))
        self.con.commit()

    def delete_all_tasks(self):
        query = 'DELETE FROM '+ self.table_name
        self.cur.execute(query)
        self.con.commit()

    def drop_table(self):
        query = 'DROP TABLE '+ self.table_name
        self.cur.execute(query)
        self.con.commit()

    def close_connection(self):
        self.con.close()