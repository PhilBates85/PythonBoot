import sqlite3

#1 connect to a database
#2 Create a cusor object "pointer"
#3 Write an SQL query
#4 commit changes
#5 Close database connection

#a varible create and connect to data base
conn=sqlite3.connect("lite.db")
#create a cusor object
cur=conn.cursor()
#point to cursor , ("Enter SQL code here")
cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
#ADD CONTENT
cur.execute("INSERT INTO store VALUES ('Wine Glass',8,10.5)")
#connect and commit changes
conn.commit()
#close connection
conn.close()

#using functions is more efficent
def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

#use function to insert values into table
def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

#inserting data using the called function
insert("Coffee Cup",10,5)

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())
