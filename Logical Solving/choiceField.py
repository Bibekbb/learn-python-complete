def per_circle(radius):
    permetor = 2*3.14*radius
    print("Perimetor of circle is : ", permetor)

def per_triangle(side1, side2, side3):
    perimeter = side1+side2+side3
    print("Permeter of triangle is: ", perimeter)

def per_rectangle(height, width):
    perimeter = 2*(height+width)
    print("Perimeter of rectangle is: ", perimeter)

def per_square(side):
    perimeter = 4*side
    print("Perimeter of square is: ", perimeter)

def a_circle(radius):
    area = 3.14*radius*radius
    print("Area of circle is: ", area)

def a_triangle(base, height):
    area = 0.2*(height*base)
    print("Area of triangle is: ", area)

def a_rectangle(height, width):
    area = height*width

def a_square(side):
    area = side *side
    print("Area of square is: ", area)


print("\n WELCOME TO MEASUREMENT PROGRAM! TRY TO CALCULATE PERIMETER AND AREA OF DIFFERENT GEOMETRIC SHAPES!!! ")

while True:
    print("\nMenu")
    print("1. Circle")
    print("2. Triangle")
    print("3. Rectangle")
    print("4. Square")
    print("5. Exit")
    shape_choice = int(input("\nEnter your choice!!!"))

    if shape_choice == 1:
        while True:
            print("\n 1. Calculate perimetoer of circle...")
            print("\n 2. Calculate area of circle...")
            print("3. Exit")

            choice1 = int(input("\n Enter choice for calculations: "))
            if choice1 == 1:
                radius = int(input("Enter radius of circle perimeter: "))
                per_circle(radius)
            elif choice1 == 2:
                radius = int(input("Enter radius of circle area: "))
                a_circle(radius)
            elif choice1 == 3:
                break
            else:
                print("Invalid Choice")
        
    elif shape_choice == 2:
        while True:
            print("\n 1. Calculate perimeter of Triangle...")
            print("\n 2. Calculate area of Trinagle...")
            print("\ 3. Exit")
            choice1 = int(input("\n Enter the choice for calculation in Triangle:"))
            if choice1 == 1:
                side1 = int(input("Enter the length of triangle side1: "))
                side2 = int(input("Enter the length of triangle side2: "))
                side3 = int(input("Enter the side of triangle side3: "))
                per_triangle(side1, side2, side3)
            elif choice1 == 2:
                break
            else:
                print("Invalid choice.")

    elif shape_choice == 3:
        while True:
            print("\n 1. Calculate perimeter of rectangle.")
            print("\n 2. Calculate area of rectangle.")
            print("\n 3. Exit")
            choice1 = int(input("\n Enter the choice of calculations: "))
            if choice1 == 1:
                height = int(input("Enter height of rectangle: "))
                width = int(input("Enter the width of rectangle: "))
                per_rectangle(height, width)
            elif choice1 == 2:
                height = int(input("Enter the height of rectangle: "))
                width = int(input("Enter the width of rectangle: "))
                a_rectangle(height, width)
            elif choice1 == 3:
                break
            else:
                print("Invalid Choice.")
    elif shape_choice == 4:
        while True:
            print("\n 1. Calculate perimeter of square...")
            print("\n 2. Calculate area of square...")
            print("\n 3. Exit")
            choice1 = int(input("Enter the choice of calculations in square..."))
            if choice1 == 1:
                side = int(input("Enter the side of square: "))
                per_square(side)
            elif choice1 == 2:
                side = int(input("Enter the side of square: "))
                a_square(side)
            elif choice1 == 3:
                break
            else:
                print("Invalid Choice.")

    elif shape_choice == 5:
        break
    else:
        print("Incorrect choice. Please try again! ")

print("Thank you for using this mini program! ")


                
        
