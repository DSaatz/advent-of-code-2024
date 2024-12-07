from re import findall
from functools import reduce
from operator import add, mul
import os

#once again someone was smarter than me: my result for task 1 was 2437273842102 contrary to this 2437272016585, which seems like I only made a slight error (eventually not iterating over all data or using wrong indices in the DP?)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

parse = lambda l: map(int, findall(r'\d+', l))
cat = lambda x, y: int(str(x) + str(y))

for ops in (add, mul), (add, mul, cat):
    f = lambda X, y: [op(x, y) for x in X for op in ops]
    print(sum(t for t, x, *X in map(parse, open(file_path))
                if t in reduce(f, X, [x])))