#modifying my solution for part 2 the way I intended didn't work out so I got inspired by the solution of user @fuglede on github who created a beautiful short solution

def checkSafety(levels):
    increasing = True
    decreasing = True

    for i in range(1, len(levels)): 
        diff = abs(levels[i] - levels[i-1])
        if diff > 3:
            return False
        
        if levels[i] <= levels[i-1]:
            increasing = False
        if levels[i] >= levels[i-1]:
            decreasing = False

    return increasing or decreasing

import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

with open(file_path) as f:
    ls = f.read().strip().split("\n")

ns = [list(map(int, re.findall(r'\d+', l))) for l in ls]

def safe2(levels):
    return any(checkSafety(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))

print(sum(safe2(l) for l in ns))