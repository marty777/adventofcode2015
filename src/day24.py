#day24.py

def quantum_entanglement(group1):
    product = 1
    for p in group1:
        product *= p
    return product    

def group_equal(groupA, groupB):
    if len(groupA) != len(groupB):
        return False
    equal = True
    for a in groupA:
        if a not in groupB:
            equal = False
            break
    return equal
    
def group_in_possibles(group, possibles):
    for p in possibles:
        if group_equal(group, p):
            return True
    return False

def package_sum(group):
    sum = 0
    for i in range(0, len(group)):
        sum += group[i]
    return sum

def group234_2(packages, group1, group2, possibleB, required_sum):
    curr_sumB = package_sum(possibleB)
    if curr_sumB > required_sum:
        return False
    if(curr_sumB == required_sum):
        return True
    
    for p in packages:
        if p in group1 or p in group2 or p in possibleB:
            continue
        if p + curr_sumB > required_sum:
            continue
        potentialB = possibleB.copy()
        potentialB.append(p)
        if group234_2(packages, group1, group2, potentialB, required_sum):
            return True
    return False
    
def group234_1(packages, group1, possibleA, required_sum):
    curr_sumA = package_sum(possibleA)
    if curr_sumA > required_sum:
        return False
    if curr_sumA == required_sum:
        return group234_2(packages, group1, possibleA, [], required_sum)
    for p in packages:
        if p in group1 or p in possibleA:
            continue
        if p + curr_sumA > required_sum:
            continue
        potentialA = possibleA.copy()
        potentialA.append(p)
        if group234_1(packages, group1, potentialA, required_sum):
           return True
    return False
                
# don't care about the actual assignments, just return true if at least one arrangment exists
def group23(packages, group1, possible, required_sum):
    curr_sum = package_sum(possible)
    viable = False
    if curr_sum == required_sum:
        return True
    for p in packages:
        if p in group1:
            continue
        if p in possible:
            continue
        if p + curr_sum > required_sum:
            continue
        potential = possible.copy()
        potential.append(p)
        if group23(packages, group1, potential, required_sum):
            viable = True
            break
    return viable

def groups1(packages, group1, required_sum, depth, required_length):
    possibles = []
    curr_sum = sum(group1)
    index = len(packages) - 1
    prev_candidate_index = -1
    if len(group1) >= required_length:
        return []
    if len(group1) > 0:
        prev_candidate = group1[len(group1) - 1]
        for i in range(0, len(packages)):
            if packages[i] == prev_candidate:
                prev_candidate_index = i
                break
    while index > prev_candidate_index:
        if packages[index] in group1:
            index -= 1
        elif packages[index] + curr_sum == required_sum:
            new_group = group1.copy()
            new_group.append(packages[index])
            if not group_in_possibles(new_group, possibles):
                possibles.append(new_group)
            index-=1
        elif packages[index] + curr_sum < required_sum:
            new_group = group1.copy()
            new_group.append(packages[index])
            groups = groups1(packages, new_group, required_sum, depth + 1, required_length)
            for g in groups:
                if not group_in_possibles(g, possibles):
                    g_new = g.copy()
                    possibles.append(g_new)
            index-=1
        else: # sum > required_sum
            index -= 1        
    return possibles

def day24(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    packages = []
    for line in lines:
        line = line.replace('\n', '')
        packages.append(int(line))
    packages.sort(reverse=True)
    
    sum = 0
    for package in packages:
        sum += package
    avg = int(sum/3)
    
    part1 = 0
    for length in range(1, len(packages)):
        min_qe_at_length = -1
        group1_possibles = groups1(packages, [], avg, 0, length)
        for g in group1_possibles:
            if len(g) < length:
                continue # previously checked
            entanglement = quantum_entanglement(g)
            if min_qe_at_length > 0 and entanglement >= min_qe_at_length:
                continue
            if not group23(packages, g, [], avg):
                continue
            if min_qe_at_length == -1 or entanglement < min_qe_at_length:
                min_qe_at_length = entanglement
        if min_qe_at_length > -1:
            part1 = min_qe_at_length
            break
            
    avg2 = int(sum/4)
    
    part2 = 0
    for length in range(1, len(packages)):
        min_qe_at_length = -1
        group1_possibles = groups1(packages, [], avg2, 0, length)
        for g in group1_possibles:
            if len(g) < length:
                continue
            entanglement = quantum_entanglement(g)
            if min_qe_at_length > 0 and entanglement >= min_qe_at_length:
                continue
            if not group234_1(packages, g, [], avg2):
                continue
            if min_qe_at_length < 0 or entanglement < min_qe_at_length:
                min_qe_at_length = entanglement
            
        if min_qe_at_length > -1:
            part2 = min_qe_at_length
            break
            
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))
    
    