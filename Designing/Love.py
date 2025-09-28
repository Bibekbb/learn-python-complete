import pyautogui as pg
import time

print("Program will run after 5 seconds.")
time.sleep(5)
print("running")

for i in range(100):
    pg.write("I Love Programming")
    time.sleep(0.5)
    pg.press("Enter")

# Importing the required module
# import pyautogui as pg
# import time

# # Giving Dealy to run program
# print("program will run after 5 second")
# time.sleep(5)
# print("running")

# # Note : after running the program immediately open whatsapp web then open the persons chat you want to send messages

# # For loop
# for i in range(100):
#     # writing the messages
#     pg.write("I love you")
#     time.sleep(0.5)
#     # Seding the messages by pressing enter
#     pg.press("Enter")