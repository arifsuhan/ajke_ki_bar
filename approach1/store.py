from generate import HelloCalendar
from db import sqlite_crud

def store_in_db(sql, data, schema):
    sql.create_connection()
    sql.create_table(schema)

    for table_data in data:
        pID = sql.insert_data(table_data)
        print(pID)
        
    sql.view_data()
    sql.close_connection()

def gen_then_store():
    
    # generate dates into list
    start_date = "27-02-2012"
    end_date = "01-03-2012"
    data = HelloCalendar("%d-%m-%Y").run(start_date, end_date)
    print(data)

    # create db, table and store the list of dates
    database = "test.db"
    table_name = "calender"
    sample_data = {  "timestamp": '01-01-1000', 
                "day" : '0', 
                "month": '1', 
                "year": '1000', 
                "day_no": '0', 
                "day_name" : 'Sunday'}
    schema = list(sample_data.keys())
    sql = sqlite_crud(database, table_name )
    store_in_db(sql,data, schema)

def query_db():
    database = "test.db"
    table_name = "calender"
    db =  sqlite_crud(database, table_name)
    db.create_connection()
    query_key = "timestamp"
    query_value = '29-02-2012'
    data = db.query_data(query_key, query_value)
    print(data)

gen_then_store()
query_db()