import random

subjects ={
    1: "MP",
    2: "DS",
    3: "ECO",
    4: "AJ",
    5: "NP"
}

random_num = random.randint(1,5)
study  = subjects[random_num]

print(study)

