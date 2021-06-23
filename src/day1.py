#day1.py

def day1(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    floor = 0
    for i in range(len(lines[0])):
        if lines[0][i] == '(':
            floor += 1
        elif lines[0][i] == ')':
            floor -= 1
    print("Part 1: %d" % floor)
    
    floor = 0
    for i in range(len(lines[0])):
        if lines[0][i] == '(':
            floor += 1
        elif lines[0][i] == ')':
            floor -= 1
        if floor == -1:
            print("Part 1: %d" % (i + 1))
            break