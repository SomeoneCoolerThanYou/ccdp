nterm = int(input("No of terms= "))
n1 = 0
n2 = 1
a = 0
if nterm <= 0:
    print("Lol")
if nterm == 1:
    print(n1)
while a<nterm:
    if a<=1:
        e = a
        print(e,end=' ')
        a+=1
    else:
        e = n1 + n2
        n1 = n2
        n2 = e
        print(e,end=' ')
        a+=1
