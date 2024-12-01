import os

column1 = []
column2 = []

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

with open(file_path) as data:
    for row in data:
        val1, val2 = row.split('   ')
        column1.append(int(val1))
        column2.append(int(val2))

similarities = []

n = len(column1)

for i in range(n):
    similarities.append(column1[i] * column2.count(column1[i]))

print(sum(similarities))
