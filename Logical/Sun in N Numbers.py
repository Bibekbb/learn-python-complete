num = int(input("Enter your numbers"))
total_sum = 0

for i in range(num):
    numbers = float(input("Enter any numbers"))
    total_sum += numbers

avg = total_sum/num
print("Avergae is:", avg)