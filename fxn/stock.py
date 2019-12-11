import sys
import csv
import mysql.connector
from mysql.connector import Error
from array import *

db_info = {"host": "localhost", "database": "pharmacy", "user": "admin", "password": "admin"}
conn = mysql.connector.connect(**db_info)
def start():
    print("LOGIN")
    u_name=str(input("ENTER USERNAME:"))
    pswd=str(input("ENTER PASSWORD:"))
    check_info(u_name,pswd)
def check_info(u_name,pswd):
    print(u_name)
    try:
        listx=[]
        sql="""select username,password from credentials"""
        cursor=conn.cursor()
        cursor.execute(sql)
        row=cursor.fetchone()
        while row is not None:
            for i in row:
                listx.append(i)
            row=cursor.fetchone()

        #print(listx)
        r=-1
        for i in range(0,len(listx)-1):
            if listx[i]==str(u_name) and listx[i+1]==str(pswd):
                print("okay")
                r=1
                break
            else:
                r=0
        if(r==1):
            stock(u_name)
        elif(r==0):
            pass

    except Error as e:
        print(e)
    finally:
        cursor.close()

def stock(u_name):
    sql1="""insert into stock (username,med_code,med_name,f_qty,med_mg) values (%s %s %s %s %s)"""
    print("You are logged in as:" + str(u_name)+"\n")
    if(u_name=="staff" or u_name=="admin"):
        while True:
            print("MENU")
            med_code=input("Enter medicine code")
            med_name=input("Enter medicine name")
            med_qty=input("Enter medicine qty")
            med_mg=input("Enter medicine mg")
            cursor=conn.cursor()
            sql2="""select med_price from stock where """
    elif(u_name=="owner"):
        owner()


def owner():
    sql1="""insert into tbl3(w_name,cp,med_code,sp) values(%s,%s,%s,%s)"""
    while True:
        try:
            cursor=conn.cursor()
            print("TASKS:\n")
            print("1.Insert in database\n2.Export")
            x=int(input("Enter your choice:"))
            if x==1:
                w_name=str(input("Enter wholesaler name:"))
                med_code=str(input("Enter medicine code:"))
                cp=int(input("Enter "+str(med_code)+" cost price:"))
                profit=float(input("Enter profit % for"+str(med_code)+" :"))
                sp=str(((cp*profit)/100)+cp)
                print(sp)
                cp1=str(cp)
                xyz = (w_name,cp1,med_code,sp)
                try:
                    cursor.execute(sql1,xyz)
                    conn.commit()
                    print("Successfully added")
                    choice=input("Do you want to continue?Y/N")
                    if(choice=="y"):

                except Error as e:
                    print(e)
                finally:
                    cursor.close()
            else:
                print("okays")
        except Error as e:
            print(e)
