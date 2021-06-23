#day14.py

def simulate(reindeer, seconds):
     distances = {}
     points = {}
     time = 0
     for name in reindeer:
        distances[name] = 0
        points[name] = 0
     while(time < seconds):
        for name in reindeer:
            reindeer[name]["phase"] = time % (reindeer[name]["length"] + reindeer[name]["rest"])
            if reindeer[name]["phase"] < reindeer[name]["length"]:
                distances[name] += reindeer[name]["speed"]
        time += 1
        max_dist = 0
        for name in reindeer:
            if distances[name] > max_dist:
                max_dist = distances[name]
        for name in reindeer:
            if distances[name] == max_dist:
                points[name] += 1
     max_dist = 0
     max_points = 0
     for name in reindeer:
        if distances[name] > max_dist:
            max_dist = distances[name] 
        if points[name] > max_points:
            max_points = points[name]
     return max_dist, max_points

    
def day14(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    f.close()
    
    reindeer = {}
    for line in lines:
        line = line.replace('\n', '')
        name, right = line.split(" can fly ")
        spd, right2 = right.split(" km/s for ")
        speed = int(spd)
        lngth, right3 = right2.split(" seconds, but then must rest for ")
        length = int(lngth)
        rst = right3.replace(" seconds.", "")
        rest = int(rst)
        reindeer[name] = {"speed":speed, "length":length, "rest":rest, "phase": 0}
    
    part1, part2 = simulate(reindeer, 2503)
    print("Part 1: %s" % (part1))
    print("Part 2: %s" % (part2))