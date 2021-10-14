#Write a program to read a list of elements. Input an element from the user that has to be inserted in
#the list. Also input the position at which it is to be inserted.

l = eval(input("Enter the list: "))
e = eval(input("Enter element to insert: "))
n = int(input("Enter the index at which to insert element: "))
l.insert(n,e)
print(l)
