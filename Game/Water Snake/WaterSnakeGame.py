import random
def check(comp , user):
    if comp == user:
        return -1
    
    if(comp == 0 and user == 1):
        return -1

    if(comp == 1 and user == 0):
        return -1
        
    if(user == 3):
        print("Invalid Number.")

    return 1

comp = random.randint(0, 2)
user = int(input("1 for Snake : 1 for Water : and 2 for Gun: "))

score = check(comp, user)

print("You: ",user)
print("Computer: ",comp)
if (score == 0):
    print("Its a draw!")
elif(score == 1):
    print("You Lose!")
else:
    print("You Won!")