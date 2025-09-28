# MAP
'''def cube(x):
    return x*x*x

print(cube(2))

l = [1,2,3,4,6,4,3]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube, l))
print(newl)'''




# FILTER

# def Filter(a):
#     return a>4

# l = [1,2,4,6,4,3]
# newl = list(filter(Filter,l))
# print(newl)

from functools import reduce

#List of numbers
# numbers = [1,2,3,4,5]
# numbers = [10,5]

# # Calculate the sum of the numbers using the reduce function



# sum = reduce(lambda x,y: x+y, numbers)
# print(sum)


# print("Bhuban Dahal")



#Map

def cube(x):
    return x*x*x

print(cube(4))
l = [1,2,4,4,5]
newl = list(map(cube, l))

print(newl)