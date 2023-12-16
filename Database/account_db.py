import sqlite3 as sql

conn= sql.connect("Database/Noted.db")
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
    sql="""
        SELECT * FROM AccountTable
        WHERE email=?
    """
    params= (email,)
    cur.execute(sql,params)
    record=cur.fetchone()
    return record
