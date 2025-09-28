# def cubes(x):
#     cube=  x ** 3
#     print(f"Your entered numbers cube is: ", cube)

# num = int(input("Enter the number you find to cube: "))
# cubes(num)

# num = input("Enter any number: ")
# num = int(num)
# for i in range(0,11):
#     print(num, 'X', i, '=', num*i)

# a = 11
# b = 10

# if a > b:
#     print("A is greater tha B")
# elif a < b:
#     print("A is smaller than B.")
# elif a == b:
#     print("A and B are equal words.")
# else:
#     ("A is equal to b.")
    

# b = 9
# b = 8
# b = 10
# print(b)

rows = int(input("Enter the number in rows: "))
for i in range(0,rows+1):
    for j in range(i):
        print("*", end="")
    print()