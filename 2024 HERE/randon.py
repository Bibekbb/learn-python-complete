# import random
# print(random.randrange(1,10))

# for x in "banana":
#     print(x)


# xe  = "Hello i am going go USA"
# print("go" in xe)


# xe  = "Hello i am going go USA"
# if "go" in xe:
#     print("Avaliable in", 'go' in xe)


# xe  = "Hello i am going go USA"
# print("show" not in xe)


# w = "working time"
# print(w.upper())

# a = "I AM GOING TO SCHOOL"
# print(a.lower())


# xe  = "Hello i am going go USA"
# print(xe.strip())


# a = "hello !"
# b = "Bibek"
# c = a+b

# print(c)

# age = 22
# print("i am", +age, "years old.")


# age = 22
# txt = "I am Bibek, and i am {} "
# print(txt.format(age))

# i = 1
# while i < 6:
#     print(i)
#     i += 1


# def MyAge():
#     age = 24
#     name = 'Bibek'
#     address = 'Lalitpur'
#     if age >= 18:
#         print("You are eligible for vote!!!")
#     else:
#         print("You are not eligible for vote!!!")

# print(MyAge)



class MyInfo():
    def __init__(self, name, age, address) :
        self.name = name
        self.age = age
        self.address = address


per = MyInfo("Bibek",22, "Lalitpur")
print(per.name)
print(per.age)