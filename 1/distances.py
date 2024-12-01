import os

column1 = []
column2 = []


#somehow regular read didn't work so I chose to do it over the os module
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

with open(file_path) as data:
    for row in data:
        val1, val2 = row.split('   ')
        column1.append(int(val1))
        column2.append(int(val2))



distances = []

while len(column1) > 0:
    distances.append(abs(column1.pop(column1.index(min(column1))) - column2.pop(column2.index(min(column2)))))

print(sum(distances))
