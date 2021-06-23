#day20.py

import math

def house_sieve(val):
    limit = int(val/10)
    limit2 = int(val/11)
    sieve = [0]*limit
    sieve2 = [0]*limit
    
    for i in range(1, len(sieve)):
        remaining = 50
        j = i
        while(j < len(sieve)):
            if remaining >= 0:
                sieve2[j] += i
                remaining-=1
            sieve[j]+=i
            j+=i
    a = 0
    b = 0
    for i in range(1,len(sieve)):
        if sieve[i]*10 >= val:
            a = i
            break
    for i in range(1, len(sieve2)):
        if sieve2[i]*11 >= val:
            b = i
            break
    return a,b
    
def day20(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    val = int(lines[0])
    
    part1,part2 = house_sieve(val)
    
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))