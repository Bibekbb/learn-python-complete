# f = open('bb.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     print(line)
#     if not line:
#         break
#     Ram = int(line.split(",")[0])
#     Shyam = int( line.split(",")[1])
#     Hari = int(line.split(",")[2])

#     print(f"Ram's Board exam marks {i} in Math: {Ram*2}")
#     print(f"Shyam's Board exam marks {i} in Math: {Shyam}")
#     print(f"Hari's Board exam marks {i} in Math: {Hari}")


#Writing file 
# f = open('bb.txt','w')
# lines = ['line 1\n', 'lines 2\n', 'lines 3 \n']
# f.writelines()
# print(lines)
# f.close()



# f = open('bb.txt','r')
# i =0
# while True:
#     i = i+1
#     line = f.readline()
#     print(line)
#     if not line:
#         break

#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]

#     print(f"Ram marks {i} in Math {m1}")
#     print(f"Shyam marks {i} in Science {m2}")
#     print(f"Hari total marks {i} in English{m3}")



#Again I'M in practicing

f = open('bb.txt', 'r')
i =0
while True:
    i = i+1
    line = f.readline()
    print(line)
    if not line:
        break
    
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"Bibek  marks {i} in Math {m1}")
    print(f"Pujan marks {i} in Nepali {m2}")
    print(f"Rupa mark {i} in Socail {m2}")