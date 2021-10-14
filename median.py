#Write a program to read a list of n integers and find their median.
#[Note: The median value of a list of values is the middle one when they are arranged in order. If
#there are two middle values then take their average. ]
#Hint: You can use an built-in function to sort the list
l = eval(input("Enter the list: "))
l.sort()
n = len(l)
if n%2 == 0:
    s = l[n/2]+l[(n/2)+1]
    print(s/2)
elif n%2 == 1:
    print(l[int((n-1)/2)])
