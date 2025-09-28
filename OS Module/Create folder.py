# a3v5c5

str1 = 'a3v5c5'
output = []
for char in str1:
    if char.isalpha():
        var = char
    else:
        num = int(char)
        output = output+(var*num)

print(output)
        