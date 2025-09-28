# s ="Hi i am Lazy Boy"
# print(s.startswith("Hi"))
# print("another".find("Other"))

# s = "The yougest people in 11 years old"
# print(s[0])
# print(s[1:3])

# l = [1,2,2].insert(2,4)
# print(len(l))

# basket = {'banana','apple','mango'}

# same = set(['banana','apple',mango])
# print(basket == same)

# same = set(['apple', 'eggs',
#  'banana', 'orange'])
# print(basket == same) 

# 

# bibek = {'banana','apple','mango'}

# same = set(['banana','apple','mango','eggs'])
# print(bibek == same)

# [('Hi ' + x) for x in ['Alice', 'Bob',
# 'Pete']]

# square = {x**2 for x in [0,4] if x <4}

# print(square)

# squares = { x**2 for x in [0,2,4] if x
# < 4 } 
# print(squares)

num1 = input("Enter first number:\n")
num2 = input("Enter second number\n")
num3 = input("Enter third number\n")

if(num1>num2 and num1>num3):
    print("Number one greatest.")
elif(num2>num1 and num2>num3):
    print("Number two is greatest.")
elif(num3>num1 and num3>num2):
    print("Number three is greatest.")
else:
    print("Invalid number.")
