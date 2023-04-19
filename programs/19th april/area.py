opt = int(input("1.Triangle Area 2. Rectangle Area 3.Square Area"))
if(opt == 1):
    base = int(input("Enter base "))
    hgt = int(input("Enter height "))
    print("Area of Triangle:",0.5*(base)*(hgt))
elif(opt == 2):
    ln = int(input("Enter length: "))
    brdt = int(input("Enter breadth: "))
    print("Area of Rectangle:",ln*brdt)
else:
    side = int(input("Enter side of a square: "))
    print("Area of square:",side*side)
