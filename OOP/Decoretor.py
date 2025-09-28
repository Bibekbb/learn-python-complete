# def hello():
#     print("Hello")

# def great(fx):
#     def mfx(*args, **kwargs): # *args for using Touple and ** kwargs for using Dictionary
#         print("Good Evening")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx

# @great 
# def hello():
#     print("Hello Bibek")

# def add(a,b):
#     print(a+b)

# hello()
# great(add)(1,2)


# def great(fx):
#     def mfx(*args, **kwargs):
#         print("Good Evening")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx

# @great
# def hello():
#     print("Hello Bibek")

# def sub(a,b):
#     print(a-b)

# hello()
# great(sub)(1,2)


def great(fx):
    def mfx(*args, **kwargs):
        print(" Good evning")
        fx(**args, **kwargs)
        print("I love you")
    return mfx

@great
def hello():
    print("Hello Pukku")

def sub(a,b):
    print(a-b)

hello()
great(sub)(10,5)

