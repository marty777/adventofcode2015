#day13.py

def eval(happiness, choices):
    keys = list(happiness.keys())
    change = 0
    for i in range(0, len(choices)):
        neighbor_low = i - 1
        neighbor_high = i + 1
        if neighbor_low < 0:
            neighbor_low = len(choices) - 1
        if neighbor_high >= len(choices):
            neighbor_high = 0
        change += happiness[keys[choices[i]]][keys[choices[neighbor_low]]]
        change += happiness[keys[choices[i]]][keys[choices[neighbor_high]]]
    return change
    
def recurse(happiness, choices):
    keys = list(happiness.keys())
    if len(choices) == len(keys):
        return eval(happiness, choices)
    max_happiness = 0
    for i in range(0, len(keys)):
        if i in choices:
            continue
        next_choice = choices.copy()
        next_choice.append(i)
        next_happiness = recurse(happiness, next_choice)
        if next_happiness > max_happiness:
            max_happiness = next_happiness
    return max_happiness
    
    
def day13(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    happiness = {}
    
    for line in lines:
        line = line.replace('\n', '')
        left, right = line.split(" happiness units by sitting next to ")
        dst = right[0:len(right)-1] # omit ., newline
        src, amt = left.split(" would ")
        amount = 0
        if amt.find("gain ") != -1:
            amount = int(amt[len("gain "):])
        else:
            amount = -int(amt[len("lose "):])
        if src not in happiness:
            happiness[src] = {}
            
        happiness[src][dst] = amount
    
    part1 = recurse(happiness, [])
    print("Part 1: %s" % (part1))
    # Add 'Me'
    happiness["Me"] = {}
    for key in happiness:
        if key == "Me":
            continue
        happiness[key]["Me"] = 0
        happiness["Me"][key] = 0
    part2 = recurse(happiness, [])
    print("Part 2: %s" % (part2))
