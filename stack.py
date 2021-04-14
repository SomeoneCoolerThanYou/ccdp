stack=[]
def pushdata(stack):
    x=int(input("enter the no"))
    stack.append(x)

def popdata(stack):
    if (len(stack)==0):
        print("empty stack")
    else:
        print("deleted element is : ",stack.pop())
    
def show(stack):
    if (len(stack)==0):
        print("empty stack")
    else:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])

ch='y'
while ch=='y' or ch=='Y':
    print("1.push data")
    print("2.pop data")
    print("3.show data")
    print("0.exit")
    n=int(input("enter your choice"))
    if n==1:
        pushdata(stack)
    elif n==2:
        popdata(stack)
    elif n==3:
        show(stack)
    else :
        break
    
