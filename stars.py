i = 1
NOrow = 1
out = i
TotalNOrows = int(input("Enter the number of rows: "))
while NOrow <= TotalNOrows:
    while i <= NOrow:
        print(out,end = '')
        i += 1
        out+=1
    print()
    i = 1

    NOrow += 1
