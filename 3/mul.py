import os
import re

mul_pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

mul_tuples = re.findall(mul_pattern, open(file_path).read())

mul_tuples = [(int(a), int(b)) for a, b in mul_tuples]

sum_of_products = sum(a * b for a, b in mul_tuples)

print(sum_of_products)