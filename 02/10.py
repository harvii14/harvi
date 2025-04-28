length = int(input("Enter length"))
width = int(input("Enter width"))

area = length * width
perimeter = (length+width) * 2

if area > perimeter:
    print("Area is greater than perimeter")
elif area == perimeter:
    print("Area is equal to perimeter")
else:
    print("Area is less than perimeter")
