#this is my sadly not working solution which I can't figure out why it doesn't work
#if anyone sees this and has any idea why it doesn't work please let me know :)


import numpy as np
import os 

xmas = "XMAS"
xmas_reversed = xmas[::-1]
xmas_len = len(xmas)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

grid = open(file_path).read().splitlines()

grid_array = np.array([list(row) for row in grid])

directions = [
    (0, 1),   
    (0, -1),  
    (1, 0),   
    (-1, 0),  
    (1, 1),   
    (-1, -1), 
    (1, -1), 
    (-1, 1),  
]

def count_occurences(array, xmas, direction):
    rows, cols = array.shape
    count = 0
    dr, dc = direction

    for r in range(rows):
        for c in range(cols):
            if 0 <= r + dr * (xmas_len -1) < rows and 0 <= c + dc * (xmas_len - 1) < cols:
                sequence = ''.join(array[r + dr * i][c + dc * i] for i in range(xmas_len))

                if sequence == xmas or sequence == xmas_reversed:
                    count += 1
    
    return count

total_occurences = sum(count_occurences(grid_array, xmas, direction) for direction in directions)

print(total_occurences // 2) #FOR WHATEVER REASON THE SOLUTION IS DOUBLE THE ACTUAL AMOUNT OF OCCURENCES