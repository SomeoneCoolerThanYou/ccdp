# Write a program to display the second largest number from a list of numbers.
l = eval(input("Enter the list: "))
m4x = l[0]
s3c = l[1]
for i in l:
    if i > m4x:
        s3c = m4x
        m4x = i
    elif i < m4x and i > s3c:
        s3c = i
print(s3c)
