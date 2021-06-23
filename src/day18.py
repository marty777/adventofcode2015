#day18.py

def print_grid(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            print(grid[i][j], end = '')
        print("")

def on_count(grid):
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == '#':
                count += 1
    return count
    
def on_neighbors(grid, x, y):
    count = 0
    start_x = x - 1
    if start_x < 0:
        start_x = 0
    end_x = x + 1
    if end_x >= len(grid[0]):
        end_x = len(grid[0]) - 1
    start_y = y - 1
    if start_y < 0:
        start_y = 0
    end_y = y + 1
    if end_y >= len(grid):
        end_y = len(grid) - 1
    for i in range(start_y, end_y + 1):
        for j in range(start_x, end_x + 1):
            if i == y and j == x:
                continue
            if grid[i][j] == '#':
                count += 1
    return count

def step(gridA, gridB, part2 = False):
    for i in range(0, len(gridA)):
        for j in range(0, len(gridA[0])):
            if part2 and  ((i == 0 and j == 0) or (i == len(gridA) - 1 and j == 0) or (i == 0 and j == len(gridA[0]) - 1) or (i == len(gridA) - 1 and j == len(gridA[0]) - 1)):
                continue
            neighbors = on_neighbors(gridA, j, i)
            if gridA[i][j] == '#' and (neighbors == 2 or neighbors == 3):
                gridB[i][j] = '#'
            elif gridA[i][j] == '.' and neighbors == 3:
                gridB[i][j] = '#'
            else:
                gridB[i][j] = '.'

def day18(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    gridA = []
    gridB = []
    steps = 100
    for i in range(0, len(lines)):
        line = lines[i].replace('\n', '')
        gridA.append([])
        gridB.append([])
        for j in range(0, len(line)):
            gridA[i].append(line[j])
            gridB[i].append(line[j])
    
    for i in range(0, steps + 1):
        if i % 2 == 0:
            step(gridA, gridB)
        else:
            step(gridB, gridA)
    
    part1 = 0
    if steps % 2 == 0:
        part1 = on_count(gridA)
    else:
        part1 = on_count(gridB)
    
    # reset grid
    for i in range(0, len(lines)):
        line = lines[i].replace('\n', '')
        for j in range(0, len(line)):
            gridA[i][j] = line[j]
            
    gridA[0][0] = '#'
    gridB[0][0] = '#'
    gridA[0][len(gridA[0]) - 1] = '#'
    gridB[0][len(gridA[0]) - 1] = '#'
    gridA[len(gridA) - 1][0] = '#'
    gridB[len(gridA) - 1][0] = '#'
    gridA[len(gridA) - 1][len(gridA[0])-1] = '#'
    gridB[len(gridA) - 1][len(gridA[0])-1] = '#'
    
    for i in range(0, steps + 1):
        if i % 2 == 0:
            step(gridA, gridB, True)
        else:
            step(gridB, gridA, True)
    
    part2 = 0
    if steps % 2 == 0:
        part2= on_count(gridA)
    else:
        part2 = on_count(gridB)
    
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))