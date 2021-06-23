#day16.py

def sue_find2(sues, analysis):
    for i in range(0, len(sues)):
        miss = False
        for prop in sues[i]:
            if prop == 'cats' or prop == 'trees':
                if sues[i][prop] <= analysis[prop]:
                    miss = True
                    break
            elif prop == 'pomeranians' or prop == 'goldfish':
                if sues[i][prop] >= analysis[prop]:
                    miss = True
                    break
            elif sues[i][prop] != analysis[prop]:
                miss = True
                break
        if not miss:
            return i + 1
    return -1

def sue_find(sues, analysis):
    for i in range(0, len(sues)):
        miss = False
        for prop in sues[i]:
            if sues[i][prop] != analysis[prop]:
                miss = True
                break
        if not miss:
            return i + 1
    return -1

def day16(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    sues = []
    index = 0
    for line in lines:
        line = line.replace('\n', '')
        props_str = line[line.find(':') + 2:]
        props =  props_str.split(', ')
        sues.append({})
        for prop in props:
            name, val = prop.split(": ")
            sues[index][name] = int(val)
        index += 1
    
    analysis = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1}
    print(analysis)
    part1 = sue_find(sues, analysis)
    part2 = sue_find2(sues, analysis)
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))
