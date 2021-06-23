#day10.py

def looknsay(string):
    result = ""
    index = 1
    curr = string[0]
    count = 1
    while index < len(string):
        if string[index] != curr:
            result += str(count) + curr
            curr = string[index]
            count = 1
        else:
            count += 1
        index += 1
    result += str(count) + curr
    return result

def day10(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close();
    
    line = lines[0].replace('\n', '')
    part1 = 0
    part2 = 0
    for i in range(0, 50):
        line = looknsay(line)
        if i == 39:
            part1 = len(line)
        elif i == 49:
            part2 = len(line)
    
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))
