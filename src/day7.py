#day7.py

OP_ASSIGN = 1
OP_AND = 2
OP_OR = 3
OP_NOT = 4
OP_LSHIFT = 5
OP_RSHIFT = 6

class Instruction:
    def __init__(self, line):
        self.arg1_num = False
        self.arg1_val = 0
        self.arg1_tag = ""
        self.arg2_num = False
        self.arg2_val = 0
        self.arg2_tag = ""
        self.assign_tag = ""
        self.op = 1
        self.args = 1
        self.handled = False
        
        left,right = line.split(" -> ")
        self.assign_tag = right
        
        if left.find(" AND ") != -1:
            self.op = OP_AND
            self.args = 2
            a,b = left.split(" AND ")
            self.arg1(a)
            self.arg2(b)
        elif left.find(" OR ") != -1:
            self.op = OP_OR
            self.args = 2
            a,b = left.split(" OR ")
            self.arg1(a)
            self.arg2(b)
        elif left.find(" LSHIFT ") != -1:
            self.op = OP_LSHIFT
            self.args = 2
            a,b = left.split(" LSHIFT ")
            self.arg1(a)
            self.arg2(b)
        elif left.find(" RSHIFT ") != -1:
            self.op = OP_RSHIFT
            self.args = 2
            a,b = left.split(" RSHIFT ")
            self.arg1(a)
            self.arg2(b)
        elif left.find("NOT ") != -1:
            self.op = OP_NOT
            self.args = 1
            a= left[len("NOT "):]
            self.arg1(a)
        else:
            self.op = OP_ASSIGN
            self.arg1(left)
            
    def arg1(self, string):
        if string.isnumeric():
            self.arg1_num = True
            self.arg1_val = int(string)
        else:
            self.arg1_tag = string
    def arg2(self, string):
        if string.isnumeric():
            self.arg2_num = True
            self.arg2_val = int(string)
        else:
            self.arg2_tag = string

def evaluate(instructions):
    wires = {}
    done = False
    while not done:
        remaining = 0
        for inst in instructions:
            if inst.handled:
                continue;
            elif inst.args == 1 and (inst.arg1_num or (inst.arg1_tag in wires)):
                arg1 = 0
                if inst.arg1_num:
                    arg1 = inst.arg1_val
                else:
                    arg1 = wires[inst.arg1_tag]
                
                if inst.op == OP_ASSIGN:
                    wires[inst.assign_tag] = arg1
                elif inst.op == OP_NOT:
                    wires[inst.assign_tag] = ~arg1
                    
                if wires[inst.assign_tag] < 0:
                    wires[inst.assign_tag] += 1 << 16
                inst.handled = True
                
            elif inst.args == 2 and (inst.arg1_num or (inst.arg1_tag in wires)) and (inst.arg2_num or (inst.arg2_tag in wires)):
                arg1 = 0
                arg2 = 0
                if inst.arg1_num:
                    arg1 = inst.arg1_val
                else:
                    arg1 = wires[inst.arg1_tag]
                if inst.arg2_num:
                    arg2 = inst.arg2_val
                else:
                    arg2 = wires[inst.arg2_tag]
                    
                if inst.op == OP_AND:
                    wires[inst.assign_tag] = arg1 & arg2
                elif inst.op == OP_OR:
                    wires[inst.assign_tag] = arg1 | arg2
                elif inst.op == OP_NOT:
                    wires[inst.assign_tag] = ~arg1
                elif inst.op == OP_LSHIFT:
                    wires[inst.assign_tag] = arg1 << arg2
                elif inst.op == OP_RSHIFT:
                    wires[inst.assign_tag] = arg1 >> arg2
                    
                if wires[inst.assign_tag] < 0:
                    wires[inst.assign_tag] += 1 << 16
                    
                inst.handled = True
            else:
                remaining += 1
        if remaining == 0:
            done = True
    return wires
    
def day7(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    instructions = []
    wires = {}
    
    for line in lines:
        line = line[:-1] # omit newline
        instructions.append(Instruction(line))
        instruction = instructions[len(instructions) - 1]
        
    wires = evaluate(instructions)
        
    part1 = wires["a"]
    print("Part 1: %d" % part1)
    
    # override assignment to b
    for i in range(0, len(instructions)):
        if instructions[i].assign_tag == "b":
            instructions[i].arg1_val = part1
        instructions[i].handled = False
    
    wires2 = evaluate(instructions)
    part2 = wires2["a"]
    
    print("Part 2: %d" % part2)