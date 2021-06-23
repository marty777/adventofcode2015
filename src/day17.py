#day17.py

def recurse(containers, choices):
    sum = 0
    required_sum = 150
    combinations = 0
    counts = {}
    for i in range(0, len(choices)):
        sum += containers[choices[i]]
    if sum > required_sum:
        return 0, counts
    elif sum == required_sum:
        test_str = ""
        for c in choices:
            test_str += str(containers[c]) + ", "
        counts[len(choices)] = 1
        return 1, counts
    else:
        last_choice = 0;
        if len(choices) > 0:
            last_choice = choices[len(choices) - 1]
        for i in range(last_choice, len(containers)):
            if i in choices:
                continue
            next_choice = choices.copy()
            next_choice.append(i)
            new_combinations, new_counts = recurse(containers, next_choice)
            combinations += new_combinations
            for c in new_counts:
                if c in counts:
                    counts[c] += new_counts[c]
                else:
                    counts[c] = new_counts[c]
    return combinations, counts

def day17(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    containers = []
    for line in lines:
        line = line.replace('\n', '')
        containers.append(int(line))
    
    containers.sort()
    
    part1, counts = recurse(containers, [])
    count_vals = list(counts.keys())
    count_vals.sort()
    part2 = 0
    if len(count_vals) > 0:
        part2 = counts[count_vals[0]]
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))