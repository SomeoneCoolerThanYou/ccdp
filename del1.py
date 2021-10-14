#Write a program to read elements of a list.
#a) The program should ask for the position of the element to be deleted from the list. Write
#a function to delete the element at the desired position in the list.
L = eval(input("Enter list: "))
x = int(input("Enter position of element to be deleted: "))
del L[x]
print(L)
