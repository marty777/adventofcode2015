#day6.py

def parseline(line):
    substr = ""
    op = 0
    if line.find("turn on ") != -1:
        substr = line[len("turn on "):]
        op = 1
    elif line.find("toggle ") != -1:
        substr = line[len("toggle "):]
        op = 2
    elif line.find("turn off ") != -1:
        substr = line[len("turn off "):]
        op = 3
    startstr, endstr = substr.split(" through ")
    start_xstr, start_ystr = startstr.split(",")
    end_xstr, end_ystr = endstr.split(",")
    start_x = int(start_xstr)
    start_y = int(start_ystr)
    end_x = int(end_xstr)
    end_y = int(end_ystr)
    
    return (op, start_x, start_y, end_x, end_y)

def day6(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    width = 1000
    height = 1000
    grid = [False]*width*height
    grid2 = [0] * width * height
    
    for line in lines:
        op,start_x,start_y,end_x,end_y = parseline(line)
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                index = x + (y * width)
                if(op == 1): # turn on
                    grid[index] = True
                    grid2[index] += 1
                elif(op == 2): #toggle
                    grid[index] = not grid[index]
                    grid2[index] += 2
                elif(op == 3): #turn off
                    grid[index] = False
                    grid2[index] -= 1
                    if grid2[index] < 0:
                        grid2[index] = 0
    count = 0
    count2 = 0
    for i in range(0, width * height):
        if grid[i]:
            count += 1
        count2 += grid2[i]
        
    print("Part 1: %d" % count)
    print("Part 2: %d" % count2)
    
    
    