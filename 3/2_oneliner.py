import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawdata.txt')

print(sum(int(x) * int(y) for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", open(file_path).read()) if (flag := (match == "do()") or (match != "don't()" and globals().get("flag", True))) and match.startswith("mul(") for x, y in [match[4:-1].split(",")]))


#this is so funny