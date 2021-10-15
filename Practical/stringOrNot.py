inp = input("Enter: ")
try:
    a = int(inp)
    print("The value is not a string")
except ValueError:
    print("The value is a string")
