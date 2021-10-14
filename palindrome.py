#To check whether a number is palindrome or not
num = int(input("Enter da number: "))
x = 0 #x = no. of digits in the number
y = 0
for i in str(num):
    x += 1
for i in range(x):
    if num%(10**i) == num//(10*(x-i)):
        y += 1
if y == x:
    print("It's a palindrome!")
