with open('bb.txt','r') as f:
    print(type(f))
    #Move to the 10th bytes in the file
    f.seek(10)
    # Read the next 5 bytes
    data = f.read()
    print(data)