#day9.py

def graphdist(graph, keys, choices):
    dist = 0
    for i in range(0, len(choices) - 1):
        dist += graph[keys[choices[i]]][keys[choices[i+1]]]
    return dist

def min_recurse(graph, keys, choices):
    min_dist = -1
    if(len(choices) == len(keys)):
        return graphdist(graph, keys, choices)
    for i in range(0, len(keys)):
        if i in choices:
            continue
        next_choices = choices.copy()
        next_choices.append(i)
        dist = min_recurse(graph, keys, next_choices)
        if min_dist < 0:
            min_dist = dist
        elif dist < min_dist:
            min_dist = dist
    return min_dist
    
def max_recurse(graph, keys, choices):
    max_dist = -1
    if(len(choices) == len(keys)):
        return graphdist(graph, keys, choices)
    for i in range(0, len(keys)):
        if i in choices:
            continue
        next_choices = choices.copy()
        next_choices.append(i)
        dist = max_recurse(graph, keys, next_choices)
        if max_dist < 0:
            max_dist = dist
        elif dist > max_dist:
            max_dist = dist
    return max_dist

def day9(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    graph = {}
    for line in lines:
        line = line.replace('\n', '')
        left, right = line.split(" = ")
        start, end = left.split(" to ")
        dist = int(right)
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        graph[start][end] = dist
        graph[end][start] = dist
    
    keys = list(graph.keys())
    choices = []
    
    min_dist = min_recurse(graph, keys, choices)
    max_dist = max_recurse(graph, keys, choices)
    
    print("Part 1: %d" % (min_dist))
    print("Part 2: %d" % (max_dist))
