a=int(input(" Enter  the number :-"))
noFactors = True
i=3
if a%2 == 0:
    print("Not prime")

while i < a :
    if a%i == 0:
        noFactors = False
        break

    elif a%i != 0:
        i+=2
if noFactors == True:
    print("Prime")
else:
    print("Not Prime")
