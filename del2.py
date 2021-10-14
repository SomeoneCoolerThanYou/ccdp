#b) The program should ask for the value of the element to be deleted from the list. Write a
#function to delete the element of this value from the list.
L = eval(input("Enter list: "))
x = eval(input("Enter value of element to be deleted: "))
L.remove(x)
print(L)
