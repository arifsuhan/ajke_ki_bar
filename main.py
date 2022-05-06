from gen import HelloCalendar
from db import sqlite_crud

def main():
    data = HelloCalendar("%d-%m-%Y").run()

    print(data)

    database = "test.db"
    table_name = "calender"
    schema = {"timestamp", "day", "month", "year", "day_no", "day_name"}

    # table_data = [ 1000, "Ahsan", 4500.00, 25 ]
        
    sql = sqlite_crud(database, table_name, schema)
    sql.create_connection()
    sql.create_table()


    for table_data in data:
        pID = sql.insert_data(table_data)
        print(pID)
        
    sql.view_data()
    # sql.update_data(pID)
    # sql.view_data()
    # sql.delete_all_tasks()
    
    # sql.drop_table()
    # sql.close_connection()

if __name__ == '__main__':
    main()