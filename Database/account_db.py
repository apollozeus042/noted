import sqlite3 as sql
from werkzeug.local import Local


local = Local()

def get_db():
    if not hasattr(local, 'db'):
        local.db = sql.connect("Database/Noted.db")
        local.db.row_factory = sql.Row
    return local.db

conn = get_db()
cur= conn.cursor()

def createAccDB():
    sql= """
        CREATE TABLE AccountTable(
            email TEXT,
            pass TEXT,
            firstName TEXT,
            middleName Text,
            lastName TEXT,
            primary key(email)
        )
    """
    cur.execute(sql)
    print("done")
    
def addAcc(email, password, fname,mname,lname):
    sql="""
        INSERT INTO AccountTable
        VALUES(?,?,?,?,?)
    """
    params= (email, password, fname,mname,lname)
    cur.execute(sql,params)
    conn.commit()

def selectAcc(email):
    conn = get_db()
    cur = conn.cursor()
    sql="""
        SELECT * FROM AccountTable
        WHERE email=?
    """
    params= (email,)
    cur.execute(sql,params)
    record=cur.fetchone()
    return record
