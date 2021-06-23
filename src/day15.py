#day15.py

# i suspect there's a faster way to find the maximum of a system of linear equations, but this is sufficient
def score(ingredients, amounts, test_calories = False):
    subtotals = {}
    #print(ingredients)
    #print(amounts)
    if test_calories:
        calories = 0
        for name in amounts:
            calories += ingredients[name]['calories'] * amounts[name]
        if calories != 500:
            return 0
    for name in ingredients:
        for prop in ingredients[name]:
            if prop == 'calories':
                continue
            if prop not in subtotals:
                subtotals[prop] = 0
            subtotals[prop] += ingredients[name][prop] * amounts[name]
    for name in subtotals:
        if subtotals[name] < 0:
            subtotals[name] = 0
            return 0    
    product = 1
    for name in subtotals:
        product *= subtotals[name]
    #print(subtotals)
    #print(product)
    return product

def choose(ingredients, amounts, test_calories = False):
    if len(amounts) == len(ingredients):
        return score(ingredients, amounts, test_calories)
    max_score = 0
    names = list(ingredients.keys())
    curr_sum = 0
    for name in amounts:
        curr_sum += amounts[name]
    for name in names:
        if name not in amounts:
            next_amounts = amounts.copy()
            for i in range(0, (101 - curr_sum)):
                next_amounts[name] = i
                scr = choose(ingredients, next_amounts, test_calories)
                if scr > max_score:
                    max_score = scr
    return max_score
def day15(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    ingredients = {}
    for line in lines:
        line = line.replace('\n', '')
        name, right = line.split(": ")
        ingredients[name] = {}
        props = right.split(", ")
        for prop in props:
            l,r = prop.split(" ")
            val = int(r)
            ingredients[name][l] = val
    
    print(ingredients)
    part1 = choose(ingredients, {})
    part2 = choose(ingredients, {}, True)
    print("Part 1: %s" % (part1))
    print("Part 2: %s" % (part2))