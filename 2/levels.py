import os

levelsList = []

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

with open(file_path) as data:
    for row in data:
        levelsList.append([int(x) for x in row.split(" ")])

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

def main():
    count = 0
    for levels in levelsList:
        if checkSafety(levels):
            count += 1
    print(count)

if __name__ == "__main__":
    main()