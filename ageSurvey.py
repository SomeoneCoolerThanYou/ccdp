#WAP to input age of N persons , calculate and display frequency of no of
#persons in different age groups.
#Age groups are : 0-20, 21- 40, 41- 60, and above 61.
a, b, c, d = 0, 0, 0, 0
n = int(input("enter the number of people\n> "))
for i in range(1,n+1):
    age = int(input("Enter age of person"+str(i)+": "))
    if age <= 20  and age > 0:
        a += 1
    if age > 20 and age < 41:
        b += 1
    if age > 40 and age < 61:
        c += 1
    if age > 61:
        d += 1
print()
print("The frequency of the different age groups are given as follows: ")
print("0-20         :", a)
print("21-40       : ", b)
print("41-60       : ", c)
print("above 61  : ", d)
