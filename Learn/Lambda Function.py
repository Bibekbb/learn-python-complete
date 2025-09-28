#Lamda function is a single expression

# def double(x):
#     return x*2

# print(double(5))

def apple(fx,value):
    return 6+fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,5,10))
print(apple(cube, 3))
#Anonymous function
print(apple(lambda x: x*x*x,2))