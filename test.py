import sys
import mysql.connector
from mysql.connector import Error
def read(uname):
    db_info={"host":"localhost","database":"pharmacy","user":"admin","password":"admin"}
    sql="""select * from main_tb where username=%s"""
    temp=(str(uname))
    try:
        conn=mysql.connector.connect(**db_info)
        cursor1=conn.cursor()
        print("For user:",uname)
        cursor1.execute(sql,temp)
        row=cursor1.fetchone()
        while row is not None:
            print(row)
            row=cursor1.fetchone()
    except Error as e:
        return(e)
    finally:
        cursor1.close()
        conn.close()
tmp="test"
read(tmp)