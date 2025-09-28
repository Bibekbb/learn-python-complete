import random

def guess(a,b):
    return random.randint(a,b)

def check(x,y):
    return y**2 == x

x = 100

left, right = 0 , x
y = guess(left, right)
while not check(x,y):
    y = guess(left, right)

print