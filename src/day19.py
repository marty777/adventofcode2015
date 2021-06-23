#day19.py

def reduce(string, dst, rules):
    curr_string = string
    steps = 0
    while(True):
        for k in rules:
            for r in rules[k]:
                while(True):
                    next_string = curr_string.replace(r, k, 1)
                    if curr_string == next_string:
                        break
                    steps += 1
                    curr_string = next_string
            if curr_string == dst:
                return steps

def replacements(string, src, replacement):
    results = []
    index = 0
    while(index < len(string)):
        index = string.find(src, index)
        if index == -1:
            break
        result = string[0:index] + replacement + string[(index + len(src)):]
        results.append(result)
        index += 1
    return results

def day19(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    rules = {}
    start = ''
    results = {}
    for i in range(0, len(lines)):
        line = lines[i].replace('\n', '')
        if i == len(lines) - 1:
            start = line
        elif i == len(lines) - 2:
            continue
        else:
            l,r = line.split(" => ")
            if l in rules:
                rules[l].append(r)
            else:
                rules[l] = []
                rules[l].append(r)
    
    
    for key in rules:
        for i in range(0, len(rules[key])):
            result = replacements(start, key, rules[key][i])
            for j in range(0, len(result)):
                if result[j] in results:
                    results[result[j]] += 1
                else:
                    results[result[j]] = 1
    part1 = len(results)
    
    part2 = reduce(start, "e", rules)
    
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))