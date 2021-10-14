#write a program to enter a string. replace and display the string in reverse order
s = input("Enter string: ")
a = s
s = ''
for i in range(1,len(a)+1):
    s += a[-1*i]
print(s)
