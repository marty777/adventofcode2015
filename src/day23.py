#day23.py

class Processor:
    def __init__(self, program):
        self.a = 0
        self.b = 0
        self.index = 0
        self.count = 0
        self.program = program.copy()
    
    def reset(self):
        self.a = 0
        self.b = 0
        self.index = 0
        self.count = 0
        
    def execute(self):
        finished = False
        while not finished:
            finished = self.execute_one()
        
    def execute_one(self):
        if self.index < 0 or self.index >= len(self.program):
            return True
        instruction = self.program[self.index]
        inst_split = instruction.split(' ')
        if inst_split[0] == 'hlf':
            if inst_split[1] == 'a':
                self.a = self.a/2
            else:
                self.b = self.b/2
            self.index += 1
        elif inst_split[0] == 'tpl':
            if inst_split[1] == 'a':
                self.a = self.a*3
            else:
                self.b = self.b*3
            self.index += 1
        elif inst_split[0] == 'inc':
            if inst_split[1] == 'a':
                self.a = self.a + 1
            else:
                self.b = self.b + 1
            self.index += 1 
        elif inst_split[0] == 'jmp':
            offset = int(inst_split[1])
            self.index += offset
        elif inst_split[0] == 'jie':
            offset = int(inst_split[2])
            if inst_split[1] == 'a,' and self.a % 2 == 0:
                self.index += offset
            elif inst_split[1] == 'b,' and self.b % 2 == 0:
                self.index += offset
            else:
                self.index += 1
        elif inst_split[0] == 'jio':
            offset = int(inst_split[2])
            if inst_split[1] == 'a,' and self.a == 1:
                self.index += offset
            elif inst_split[1] == 'b,' and self.b == 1:
                self.index += offset
            else:
                self.index += 1
        else:
            print("Instruction error", instruction)
            return True
        
        self.count += 1
        return False
        
def day23(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    program = []
    for line in lines:
        line = line.replace('\n', '')
        program.append(line)
    
    processor = Processor(program)
    processor.execute()
    part1 = processor.b
    
    processor.reset()
    processor.a = 1
    processor.execute()
    part2 = processor.b
    print("Part 1: %d" % (part1))
    print("Part 2: %d" % (part2))
