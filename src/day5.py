#day5.py

def vowels(string):
    vowel_str = "aeiou"
    count = 0
    for c in string:
        if c in vowel_str:
            count+=1
    if count >= 3:
        return True
    return False

def doubles(string):
    for i in range(0, len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False
    
def nobadstrings(string):
    bad = ['ab', 'cd', 'pq','xy']
    for b in bad:
        if string.find(b) != -1:
            return False
    return True

def doubledouble(string):
    for i in range(0, len(string) - 2):
        substr = string[i:i+2]
        if string.find(substr, i+2) != -1:
            return True
    return False
    
def doublehop(string):
    for i in range(0, len(string) - 2):
        if string[i] == string[i+2]:
            return True
    return False        

def day5(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    nice_count = 0
    nice_count2 = 0
    for line in lines:
        nice = vowels(line) and doubles(line) and nobadstrings(line)
        nice2 = doubledouble(line) and doublehop(line)
        if nice:
            nice_count += 1
        if nice2:
            nice_count2 += 1
    
    print("Part 1: %d" % (nice_count))
    print("Part 2: %d" % (nice_count2))
    
    