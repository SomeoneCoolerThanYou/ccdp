#Write a program to read a list of n integers (positive as well as negative).
#Create two new lists, one having all positive numbers and the other
#having all negative numbers from the given list. Print allthree lists

OG = eval(input("Enter the list: "))
p, n = [], []
for i in OG:
    if i > 0:
        p.append(i)
    elif i < 0:
        n.append(i)
print(OG, p, n)
