#day3.py

def day3(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    pos_x = 0
    pos_y = 0

    positions = {}
    pos_temp = "{x}x{y}"
  

    # initial position
    pos_str = pos_temp.format(x = 0, y = 0)
    positions[pos_str] = 1
    
    for i in range(0, len(lines[0])):
        if lines[0][i] == '>':
            pos_x += 1
        elif lines[0][i] == '<':
            pos_x -= 1
        elif lines[0][i] == '^':
            pos_y += 1
        elif lines[0][i] == 'v':
            pos_y -= 1
        
        pos_str = pos_temp.format(x = pos_x, y = pos_y)
        if pos_str in positions:
            positions[pos_str] += 1
        else:
            positions[pos_str] = 1

    print("Part 1: %d" % (len(positions)))
    
    positions = {}
    
    pos1_x = 0
    pos1_y = 0
    pos2_x = 0
    pos2_y = 0
    
    pos_str = pos_temp.format(x = 0, y = 0)
    positions[pos_str] = 2
    
    for i in range(0, len(lines[0])):
        if lines[0][i] == '>':
            if i % 2 == 0:
                pos1_x += 1
            else:
                pos2_x += 1
        elif lines[0][i] == '<':
            if i % 2 == 0:
                pos1_x -= 1
            else:
                pos2_x -= 1
        elif lines[0][i] == '^':
            if i % 2 == 0:
                pos1_y += 1
            else:
                pos2_y += 1
        elif lines[0][i] == 'v':
            if i % 2 == 0:
                pos1_y -= 1
            else:
                pos2_y -= 1
        
        if i % 2 == 0:
            pos_str = pos_temp.format(x = pos1_x, y = pos1_y)
        else:
            pos_str = pos_temp.format(x = pos2_x, y = pos2_y)
        if pos_str in positions:
            positions[pos_str] += 1
        else:
            positions[pos_str] = 1
        
                
    print("Part 2: %d" % (len(positions)))
    