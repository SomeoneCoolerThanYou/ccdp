import pickle as p
def adddata():
    f=open("bank.dat","ab")
    acno=int(input("enter the account no"))
    name=input("enter the name")
    bal=int(input("enter the balance"))
    rec=[acno,name,bal]
    p.dump(rec,f)
    f.close()

def show():
    f=open("bank.dat","rb")
    while True:
        try:
            rec=p.load(f)
            print(rec)
        except:
            break
    f.close()


while True:
    print("1.add data")
    print("2.sho data")
    print("0.exit")
    n=int(input("enter your choice"))
    if n==1:
        adddata()
    elif n==2:
        show()
    else :
        break

    
            
