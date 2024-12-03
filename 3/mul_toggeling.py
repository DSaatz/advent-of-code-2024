import os
import re

#Woho today I came up with using regex efficently myself! :D (well kinda I did something similiar but it failed then saw a meme on reddit with pretty much the same solution lol) 



pattern = r"mul\((-?\d+),\s*(-?\d+)\) | do\(\) | don't\(\)"



script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawdata.txt')

matches = re.findall(pattern, open(file_path).read())

flag = True
result = 0


for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            x, y = map(int, match[4:-1].split(",")) #this throws an error???
            result += x * y


print(result)