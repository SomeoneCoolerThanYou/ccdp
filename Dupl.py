#Write a program to read a list of elements. Modify this list so that it does not contain any duplicate
#elements, i.e., all elements occurring multiple times in the list should appear only once

L = eval(input("Enter the list: "))
L.sort()
for i in L:
    print("I got",i)
    while i in L:
        L.remove(i)
        print("REMOVING",i)
    L.append(i)
    print("ADDING",i)
print(L)
