import numpy as np
import os

mas = "MAS"
mas_reversed = mas[::-1]

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

grid = open(file_path).read().splitlines()

grid_array = np.array([list(row) for row in grid])

rows, cols  = grid_array.shape

def is_xmas(array, r, c):

    positions_top_left = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]  
    positions_bottom_left = [(r + 1, c - 1), (r, c), (r - 1, c + 1)]  

    
    if not all(0 <= x < rows and 0 <= y < cols for x, y in positions_top_left + positions_bottom_left):
        return False

    
    diagonal1 = "".join(array[x, y] for x, y in positions_top_left)
    diagonal2 = "".join(array[x, y] for x, y in positions_bottom_left)

    
    return ((diagonal1 == mas or diagonal1 == mas_reversed) and
            (diagonal2 == mas or diagonal2 == mas_reversed))

count = sum(is_xmas(grid_array, r, c) for r in range(rows) for c in range(cols))

print(count)