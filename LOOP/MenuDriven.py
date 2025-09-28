def per_circle(radius):
    perimeter = 2*3.14*radius
    print("Perimeter of circle is :", perimeter)
def per_triangle(side1 , side2 ,side3):
    perimeter = side1+side2+side3
    print("Perimeter of triangle is :", perimeter)
def per_rectangle(height,width):
    perimeter = 2* (height+width)
    print("Perimeter of rectangle is :", perimeter)
def per_square(side):
    perimeter = 4*side
    print("Perimeter of square is :", perimeter)
def a_circle(radius):
    area = 3.14*radius*radius
    print("Area of circle is :",area )
def a_triangle(base,height):
    area = 0.2*height*base
    print("Area of circle is:",area)
def a_rectangle(height,width):
    area = height * width
    print("Area of rectangle is :",area)
def a_square(side):
    area = side*side
    print("Area of square is :",area)

print("\nWELCOME TO MEASURATION PROGRAM! TRY TO CALCULATE PERIMETER AND AREA OD DIFFERENT GEOMETRIC SHAPES!")

while True:
    print("\nMENU")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Exit")
    shape_choice = int(input("\nEnter your choice!"))

    if shape_choice == 1:
        while True:
            print("\n1. Calculate perimeter of circle.")
            print("\n2. Calculate area of circle.")
            print("3. exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1== 1:
                radius = int(input("Enter radius of circle: "))
                per_circle(radius)
            elif choice1 == 2:
                radius = int(input("Enter Radius of circle: "))
                a_circle(radius)
            elif choice1 == 3:
                break
            else:
                print("Invalid choice.")

    elif shape_choice == 2:
        while True:
            print("\n1. calculate perimeter of Triangle.") 
            print("2. Calculate area of Triangle. ")
            print("3. exit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                side1 = int(input("Enter length of side1: "))
                side2 = int(input("Enter length of side2: "))
                side3 =int(input("Enter length of side3:  "))
                per_triangle(side1,side2,side3)
            elif choice1 == 3:
                break
            else:
                print("Invalid choice.")
                
    elif shape_choice == 3:
        while True:
            print("\n1. Calculate perimeter of rectangle")
            print("\n2. Calculate area of rectangle.")
            print("\nExit")
            choice1 = int(input("\nEnter choice for calculations: "))
            if choice1 == 1:
                height = int(input("Enter height for rectangle: "))
                width = int(input("Enter width for rectangle: "))
                per_rectangle(height, width)
            elif choice1 == 2:
                height = int(input("Enter height of rectangle: "))
                width = int(input("Enter width of rectangle: "))
                a_rectangle(height,width)
            elif choice1 == 3:
                break
            else:
                print("Invalid choice.")

    elif shape_choice == 4:
        while True:
            print("\n1. Calculate perimeter of square.")
            print("\n2. Calculate area of square.")
            print("\n3. Exit.")
            choice1 = int(input("Enter choice of calculations:"))
            if choice1 == 1:
                side = int(input("Enter side of square: "))
                per_square(side)
            elif choice1 == 2:
                side = int(input("Enter side of square: "))
                per_square(side)
            elif choice1 == 3:
                break
            else:
                print("Invalid choice.")

    elif shape_choice == 5:
        print("Thank you ! See you again.")
        break
    else:
        print("Incorrect choice. Plese try again!")

print("Thank you for using this program.3")
 