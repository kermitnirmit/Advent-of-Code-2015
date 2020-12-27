import hashlib

i = 1
base = "ckczppom"

while True:
    str2hash = "ckczppom" + str(i)
    
    # encoding GeeksforGeeks using encode() 
    # then sending to md5() 
    result = hashlib.md5(str2hash.encode()) 
    
    # printing the equivalent hexadecimal value. 
    # print(result.hexdigest()[:5]) 

    if result.hexdigest()[:6] == "000000":
        break
    if i % 500000 == 0:
        print("progress: ", i)
    i += 1
print(i)