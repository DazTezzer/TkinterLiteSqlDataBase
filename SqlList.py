import sqlite3 as sl

con = sl.connect('test.db')
P_In_sql = "INSERT INTO Products (name,num,price,picture) values(?,?,?,?)"
P_Del_sql = "DELETE from Products where id = "
P_Ch_sql = "Update Products set name = ?, num = ?, price = ?, picture = ? where id = ?"

def Create():
    with con:
        con.execute(
            """CREATE TABLE IF NOT EXISTS Products  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, num INTEGER, price INTEGER,picture TEXT);""")
        con.execute(
            """CREATE TABLE IF NOT EXISTS Clients (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, tel TEXT, code INTEGER);""")
        con.execute(
            """CREATE TABLE IF NOT EXISTS Trade (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, num INTEGER, code INTEGER);""")


def PTableGet():
    with con:
        table = con.execute("Select * From Products")
    return table


def Add(sql,Data):
    with con:
        con.executemany(sql, Data)


def Del(sql):
    con.execute(sql)


def Change(sql,Data):
    con.execute(sql,Data)