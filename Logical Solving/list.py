# basket = {'Apple','Banana','Manago','Watermelon'}

# print('Apple' in basket)

# print('eggs' in basket)


# x = 55/11
# print(x)

# x = 50*2 + (60-20) /4
# print(x)

# x = 'silent'
# print(x[2] + x[1] + x[0]
# + x[5] + x[3] + x[4])


# squares = [1,4,9,16,25]
# print(squares[0])

# word = 'galaxy'
# print(len(word[1:]))

# print(3 * 'un' + 'inm')

# print(3 * 'bb' '\n' + 'ibek')

# print(sum(range(0, 7)))

# print(0+1+2+3+4+5+6)

# cubes = [1, 8, 27]
# cubes.append(4 ** 3)

# cubes.append(5 ** 3)
# print(cubes)

# def cubes(x):
#     return x ** 3

# num1 = int(input("Enter any number: "))

# print(num1 in 0)

# word = 'galaxy'
# print(word[4:50])

# x = 51 % 3
# print(x)


def if_confusion(x ,y):
    if x > y:
        if x - 5 > 0:
            x = y
            return "A" if y == y + y else "B"
        elif x + y > 0:
            while x > y : x -= 1
            while y > x: y -= 1
            if x == y:
                return "E"        
    else:
        if x - 2 > y - 4:
            x_old = x
            x = y * y
            y = 2 * x_old
            if (x-4) **2 > (y - 7) ** 2:
                return "C"
            return "D"
        return "H"
    
print(if_confusion(3,7))






