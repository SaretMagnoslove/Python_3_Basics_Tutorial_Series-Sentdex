import sqlite3

conn = sqlite3.connect('tutorial.db') # connecting or creating the db
c = conn.cursor() # creating a cursor to execute sql commands
# creating the table
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")
# inserting data into the table
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")

    conn.commit() # commiting the data into the table
    c.close() # closing the cursor
    conn.close() # closing the connection
    
create_table()
data_entry()