#program to find area of a triangle using Heron's formula
a = float(input("Enter the length of the first side of the Triangle: "))
b = float(input("Enter the length of the second side of the Triangle: "))
c = float(input("Enter the length of the third side of the Triangle: "))

s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the Triangle is ', area, 'units')
