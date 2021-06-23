#day4.py

import hashlib

def day4(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    key = lines[0]
    found1 = False
    found2 = False
    result1 = 0
    result2 = 0
    
    index = 1
    
    while not found1 or not found2:
        test_str = key + str(index)
        result = hashlib.md5(test_str.encode())
        digest = result.hexdigest()
        if digest.find("00000") == 0 and not found1:
            print(test_str)
            print(digest)
            found1 = True
            result1 = index
        if digest.find("000000") == 0 and not found2:
            print(test_str)
            print(digest)
            found2 = True
            result2 = index
        index += 1
    
    print("Part 1: ", (result1))
    print("Part 2: ", (result2))
    
    