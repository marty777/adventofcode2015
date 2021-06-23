#day8.py

def is_hex(c):
    if ord(c) in range(ord('0'), ord('9')+1) or ord(c) in range(ord('a'), ord('f')+1):
        return True
    return False

def memlen(string):
    last = ''
    count = 0
    index = 1
    if string[0] != '"' or string[len(string) - 1] != '"':
        print("Possible quote problem", string)
    while index < len(string) - 1:
        if string[index] == '\\':
            if string[index+1] == '\\':
                count += 1
                index += 2
            elif string[index+1] == '"':
                count += 1
                index += 2
            elif string[index+1] == 'x' and is_hex(string[index+2]) and is_hex(string[index + 3]):
                count += 1
                index += 4
            else:
                print("\tUNESCAPED", string[index+1], is_hex(string[index+2]), is_hex(string[index+3]))
                count += 1
                index += 1
        else:
            count += 1
            index += 1
    return count

def encode(string):
    string = string.replace('\\', '\\\\')
    string = string.replace('"', "\\\"")
    return string
    

def day8(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    char_count = 0
    mem_count = 0
    enc_count = 0
    for line in lines:
        line_trunc = line.replace("\n", "")
        line_len = len(line_trunc)
        mem_len = memlen(line_trunc)
        line2 = encode(line_trunc)
        enc_count += 2 + len(line2)
        char_count += line_len
        mem_count += mem_len
    
    print("Part 1: %d" % (char_count - mem_count))
    print("Part 2: %d" % (enc_count - char_count))