import time
# def usingwhile():
#     while i<5000:
#         i = i+1
#         print(i)
    

# def usingFor():
#     for i in range(5000):
#         print(i)

# init = time.time() 
# usingFor()
# print(time.time() -init)
# t1 = time.time()
# usingwhile()
# print(time.time()-init)
# print(t1)

# print(4)
# time.sleep(3)
# print("This is printed afer 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%y-%m-%d %H:%M:%S",t)
print(formatted_time)