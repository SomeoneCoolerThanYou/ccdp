import mysql.connector as con
def createdatabase():
    db=con.connect(host="localhost",user="root",passwd="amit")
    cur=db.cursor()
    cur.execute("create database demo")
    print("database created")
    db.close()

def createtable():
    db=con.connect(host="localhost",user="root",passwd="amit",database="demo")
    cur=db.cursor()
    query="create table emp(eno int(5),name varchar(20),age int(2))"
    cur.execute(query)
    print("table created")
    db.close()

def adddata():
    db=con.connect(host="localhost",user="root",passwd="amit",database="demo")
    cur=db.cursor()
    eno=int(input("enter the eno"))
    name=input("enter the name")
    age=int(input("enter the age"))
            
    query="insert into emp values({},'{}',{})"
    cur.execute(query.format(eno,name,age))
    db.commit()
    print("record added")
    db.close()

   
def showdata():
    db=con.connect(host="localhost",user="root",passwd="amit",database="demo")
    cur=db.cursor()          
    query="select * from emp"
    cur.execute(query)    
    rec=cur.fetchall()
    for i in rec:
        print(i)
    
    db.close()
    

ch='y'
while ch=='Y' or ch=='y':
    print("1.create database")
    print("2.create table")
    print("3.add data")
    print("4. show")
    print("0.exit")
    n=int(input("enter your choice..."))
    if n==1:
        createdatabase()
    elif n==2:
        createtable()
    elif n==3:
        adddata()
    elif n==4:
        showdata()
    elif n==0:
        break
    ch=input("do you want to continue..")
    








