print("Type c for calculating area of circle, ", end='')
print("s for calculating the area of square and r for calculating the area of a rectangle: ")
wubbalubbadubdub = str(input('> '))
if wubbalubbadubdub == 'c':
    r = int(input("Enter Radius: "))
    print("The area is",3.14*r*r,' square units')
elif wubbalubbadubdub == 's':
    s = int(input("Enter the side of the square: "))
    print("The area is",s*s,' square units')
elif wubbalubbadubdub == 'r':
    l = int(input("Enter length of the rectangle: "))
    b = int(input("Enter breadth of the rectangle: "))
    print("The area is",l*b,' square units')
