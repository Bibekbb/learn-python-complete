'''  while True:
    print("Menu driven program.")
    print("1. Area of Circle.")
    print("2.Area of Rectangle.")
    print("3.Area of Square.")
    print("2. Exit.")
    choice =int(input("\nEnter your choice: "))
    if choice == 1:
        radius =int(input("Enter radious of circle? "))
        print("Area of circle",3.14*radius*radius)
    elif choice == 2:
        length = int(input("Enter length of Rectangle?"))
        breadth = int(input("Enter breadth of Rectangle?"))
        print("Area of rectangle=",length*breadth)
    elif choice == 3:
        side = int(input("Enter side of Square? "))
        print("Area of Square =",side*side)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
    repeat = input("Do you want to continue ? (y/n)")
    if repeat == 'n' or repeat == 'N':
        break  '''



'''while True:
    print("Which item you need?")
    print("1. Coffee")
    print("2. Tea")
    print("3. Cold drinks")
    print("4. Exit")
    choice = int(input("Enter your choice? "))
    if choice == 1:
        print(" Milk Coffee or Black Coffee? ")
        item = ['Black', 'Milk']
        print(f"{item}")
    elif choice == 2:
        print("Black tea and Milk tea? ")
        item = ['Black','Milk']
        print(f"{item}")
    elif choice == 3:
        item = set('coca Cola','Pepsi','Dew','Slice','Mirinda')
        print(f(item))
        break
    else:
        print("Invalid choice.")
    repeat =input("Do you want to continue? (y/n)")
    if repeat == 'n' or repeat == 'N':
        break'''


age = int(input("Enter your age"))
if age > 18 :
    print("Your are eligible for voting.")
else:
    print("You are not eligible for voting.")
    
