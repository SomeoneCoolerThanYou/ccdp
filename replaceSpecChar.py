#write a program o enter a string with special characters and display it without them
s = input("Enter the string: ")
for i in s:
    if not i.isalnum():
        s = s.replace(i,'')
print(s)
