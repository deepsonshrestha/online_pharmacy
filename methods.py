import sys
import csv
import mysql.connector
from mysql.connector import Error
from array import *
abc=1
def choice():
    print("Login:")
    username=input("Enter your username:")
    password=input("Enter your password:")
    database(username,password)
def database(uname,pswd):
    db_info={"host":"localhost","database":"pharmacy","user":"admin","password":"admin"}
    try:
        listx = []
        conn=mysql.connector.connect(**db_info)
        if conn.is_connected():
            print("Connected to table")
            cursor=conn.cursor()
            cursor.execute("select username,password from credentials")
            '''row=cursor.fetchone()
            while row is not None:
                x+=1
                row=cursor.fetchone()
            print("X=",x)'''
            row = cursor.fetchone()

            while row is not None:
                for i in row:
                    listx.append(i)
                row = cursor.fetchone()
        #print(listx)
        r=""
        for i in range(0,len(listx)-1):
            if listx[i]==uname and listx[i+1]==pswd:
                r="LOGGED IN"
                break
            else:
                r="INVALID CREDENTIALS"
        print(r)
        if(r=="LOGGED IN"):
            menu(uname)
    except Error as e:
        print("Error:",e)
    finally:
        pass
def menu(uname):
    while abc==1:
        print("MENU\n")
        print("1.Insert data\n2.Read from table\n3.Search\n4.Delete data\n5.Update\n6.Export to file \n7.Backup database\n8.Restore database")
        choice=int(input("Enter your choice:"))
        if choice==1:
            insert(uname)
        elif choice==2:
            read(uname)
        elif choice==3:
            search(uname)
        elif choice==4:
            delete(uname)
        elif choice==5:
            update(uname)
        elif choice==6:
            export_f(uname)
        elif choice==7:
            backup_d(uname)
        elif choice==8:
            restore_d(uname)
        else:
            return("Invalid choice!!")

def insert(uname):
    db_info={"host":"localhost","database":"pharmacy","user":"admin","password":"admin"}
    sql="""insert into main_tb(username,med_name,med_mg,med_code,med_price) values(%s,%s,%s,%s,%s) """
    med_name=input("Enter name of medicine:")
    med_mg=input("Enter mg of "+med_name)
    med_code=input("Enter "+med_name+" code")
    med_price = input("Enter " + med_name + " price")
    values=[uname,med_name,med_mg,med_code,med_price]
    if(med_name.isalpha() == True and med_mg.isnumeric() == True and med_code.isalnum() == True and med_price.isnumeric() == True):
        try:
            conn=mysql.connector.connect(**db_info)
            cursor=conn.cursor()
            cursor.execute(sql,values)
            conn.commit()
            print("Data inserted successfully")
        except Error as e:
            print("Error:",e)
        finally:
            cursor.close()
            conn.close()
    else:
        print("Invalid datatypes")
def read(uname):
    db_info={"host":"localhost","database":"pharmacy","user":"admin","password":"admin"}
    sql="""select * from main_tb where username=%s"""
    temp=[str(uname)]
    try:
        conn=mysql.connector.connect(**db_info)
        cursor=conn.cursor()
        print("For user:",uname)
        cursor.execute(sql, temp)
        row=cursor.fetchone()
        while row is not None:
            print(row)
            row=cursor.fetchone()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def update(uname):
    db_info={"host":"localhost","database":"pharmacy","user":"admin","password":"admin"}
    sql="""update main_tb 
            set med_name=%s,
                med_mg=%s,
                med_price=%s
            where med_code=%s"""
    temp_code = input("Enter desired medicine's code that is to be altered:")
    listz=[]
    try:
        conn=mysql.connector.connect(**db_info)
        cursor=conn.cursor()
        cursor.execute("select * from main_tb")
        row=cursor.fetchone()
        while row is not None:
            for i in row:
                listz.append(i)
            row=cursor.fetchone()
        print(listz)
        for j in range(0,len(listz)):
            if str(listz[j])==str(temp_code):
                r=1
                break
            else:
                r=0
        if(r==1):

            temp_name = input("Enter the name of " + temp_code + " that is to be updated:")
            temp_mg = input("Enter the mg of " + temp_code + " that is to be updated:")
            temp_price = input("Enter the price of " + temp_code + " that is to be updated:")
            temp = [str(temp_name), str(temp_mg), str(temp_price), str(temp_code)]
        cursor.execute(sql, temp)
        conn.commit()
        print("Successfully updated") #return doesnot work
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
def delete(uname):
    db_info = {"host": "localhost", "database": "pharmacy", "user": "admin", "password": "admin"}
    sql="""delete from main_tb where med_code=%s"""
    temp_code=input("Enter medicine code that's record is to deleted:")
    temp=[(temp_code)]
    listy = []
    r=-1
    try:
        conn = mysql.connector.connect(**db_info)
        cursor = conn.cursor()
        cursor.execute("select med_code from main_tb")
        row = cursor.fetchone()

        while row is not None:
            for i in row:
                listy.append(i)
            row=cursor.fetchone()
        #print(listy)
        for j in range(0,len(listy)):
            if str(listy[j])==str(temp_code):
                r=1
                break
            else:
                r=0
        if(r==1):
            cursor.execute(sql, temp)
            conn.commit()
            print("Successfully deleted")  #return garna milena
        else:
            print("Failed to delete")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def export_f(uname):
    db_info = {"host": "localhost", "database": "pharmacy", "user": "admin", "password": "admin"}
    sql1="""select * from main_tb where med_code=%s"""
    file1="lalu.txt"
    file2="lalu.csv"
    file3="lalu.pdf"
    listz=[]
    listx=[]
    temp_code=input("Enter the medicines code that is to be exported: ")
    temp=[(temp_code)]
    try:
        conn=mysql.connector.connect(**db_info)
        cursor=conn.cursor()
        cursor.execute("select med_code from main_tb")
        row=cursor.fetchone()
        while row is not None:
            for i in row:
                listz.append(i)
            row=cursor.fetchone()
        print(listz)
        for k in range(0,len(listz)):
            if(str(listz[k])==str(temp_code)):
                print("hi")
                cursor.execute(sql1,temp)
                row=cursor.fetchone()
                while row is not None:
                    for i in row:
                        listx.append(i)
                    row=cursor.fetchone()
                print("Do you want to export"+temp_code+" data into\n1.Text\n2.CSV\n3.Pdf")
                choice=int(input("Enter your choice"))
                if(choice==1):
                    file=open(file1,"a")
                    file.writelines(str(listx)+"\n")
                    file.close()
                elif(choice==2):
                    file=open(file2,'a')
                    file.writelines(str(listx)+"\n")
                    file.close()
    except Error as e:
        print(e)
    finally:

        cursor.close()
        conn.close()