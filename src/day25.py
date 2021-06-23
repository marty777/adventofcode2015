#day25.py

def next(prev):
    ret = prev * 252533
    return ret % 33554393

def day25(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    line = lines[0].replace('To continue, please consult the code grid in the manual.  Enter the code at row ', '')
    line = line.replace('.\n', '')
    row_str,col_str = line.split(', column ')
    
    row = int(row_str)
    col = int(col_str)
    
    part1 = 0
    curr = 20151125
    r = 2
    c = 1
    step = 2    
    while(True):
        curr = next(curr)
        if r == row and c == col:
            part1 = curr
            break
        if r == 1:
            r = c + 1
            c = 1
        else:
            r = r - 1
            c = c + 1
        step += 1
       
    print("Part 1: %d" % (part1))
    
    