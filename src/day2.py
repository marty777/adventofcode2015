#day2.py

class Present:
    def __init__(self, line):
        ls,ws,hs = line.split("x");
        self.l = int(ls)
        self.w = int(ws)
        self.h = int(hs)
    def area(self):
        return 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l
    def extra(self):
        a = self.l*self.w
        b = self.w*self.h
        c = self.h*self.l
        return min(a,b,c)
    def ribbon(self):
        a = 2*(self.l) + 2*(self.h)
        b = 2*(self.w) + 2*(self.h)
        c = 2*(self.w) + 2*(self.l)
        return min(a,b,c)
    def vol(self):
        return (self.w * self.h * self.l)
   

def day2(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    presents = []
    for line in lines:
        presents.append(Present(line))
    
    paper = 0
    ribbon = 0
    for i in range(0, len(presents)):
        paper += presents[i].area() + presents[i].extra()
        ribbon += presents[i].ribbon() + presents[i].vol()
        
    print("Part 1: %d" % paper)
    print("Part 2: %d" % ribbon)