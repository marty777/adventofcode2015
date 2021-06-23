#day11.py

def increment(string):
    if(len(string) < 2):
        print("string length issue")
        return ""
    result = ""
    carry = 1
    
    index = len(string) - 1
    while(carry > 0 and index >= 0):
        last_char = ord(string[index]) + 1
        if last_char > 122:
            last_char = 97
            carry = 1
        else:
            carry = 0
        result = chr(last_char) + result
        index-=1
    result = string[0:index+1] + result
    return result

def check_straight(string):
    for i in range(0, len(string) - 2):
        if ord(string[i]) == ord(string[i+1]) - 1 and ord(string[i+1]) == ord(string[i+2]) - 1:
            return True
    return False

def check_forbidden(string):
    if string.find('i') != -1 or string.find('o') != -1 or string.find('l') != -1:
        return False
    return True

def check_pairs(string):
    pair1 = False
    index = 0
    pair2 = False
    for i in range(0, len(string) - 3):
        if string[i] == string[i+1]:
            pair1 = True
            index = i+2
            break
    if not pair1:
        return False
    
    for i in range(index, len(string) - 1):
        if string[i] == string[i+1]:
            pair2 = True
            break
    
    return pair2
    
def day11(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    line = lines[0].replace('\n', '')
    part1 = increment(line)
    while not (check_straight(part1) and check_forbidden(part1) and check_pairs(part1)):
        part1 = increment(part1)
    part2 = increment(part1)
    while not (check_straight(part2) and check_forbidden(part2) and check_pairs(part2)):
        part2 = increment(part2)
        
    print("Part 1: %s" % (part1))
    print("Part 2: %s" % (part2))