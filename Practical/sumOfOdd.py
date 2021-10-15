#Write a Python program to find the sum of all odd the number from a N
#numbers entered by the user.
n = int(input('Enter the number of numbers you are going to enter: '))
sum = 0
for i in range(1,n+1):
    num = int(input("Enter number "+str(i)+ " : "))
    if num % 2 != 0:
        sum += num
print(sum)
