#day12.py

import json



def recurse_sum(data, ignore_red):
    sum = 0
    red_found = False
    if type(data) is dict:
        if not ignore_red:
            for key in data:
                if data[key] == "red":
                    red_found = True
                    break
            if red_found:
                return 0
        #print("dict", data)
        for key in data:
            #print(key, data[key], type(data[key]))
            if type(data[key]) is int:
               sum += data[key]
            else:
                sum += recurse_sum(data[key], ignore_red)
    elif type(data) is list:
        #print("list", data)
        for i in range(0, len(data)):
             if type(data[i]) is int:
                sum += data[i]
             else:
                sum += recurse_sum(data[i], ignore_red)
    elif type(data) is int:
        sum += data
        
    return sum

def day12(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    result = json.loads(lines[0])
    part1 = recurse_sum(result, True)
    part2 = recurse_sum(result, False)
    print("Part 1: %s" % (part1))
    print("Part 2: %s" % (part2))