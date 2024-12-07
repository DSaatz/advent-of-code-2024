#Using DP for O(n^3) time complexity instead of bruteforce 0(2^(n-1))

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'rawData.txt')

results_and_variables = {}

with open(file_path, "r") as f:
    for line in f:
        parts = line.split(":")
        result = int(parts[0].strip())
        variables = list(map(int, parts[1].strip().split()))

        results_and_variables[result] = variables

def checkIfPossible(result, variables):
    n = len(variables)
    # DP table initialization, each entry holds a set of possible results
    dp = [[set() for _ in range(n)] for _ in range(n)]

    # Base case: each variable on its own
    for i in range(n):
        dp[i][i].add(variables[i])

    # Fill DP table for all subarray lengths
    for length in range(2, n + 1):  # subarray length from 2 to n
        for i in range(n - length + 1):
            j = i + length - 1  # The endpoint of the subarray
            # Try every possible split point
            for k in range(i, j):
                # Combine results from dp[i][k] and dp[k+1][j] using '+' and '*'
                for left in dp[i][k]:
                    for right in dp[k+1][j]:
                        dp[i][j].add(left + right)
                        dp[i][j].add(left * right)
    
    # Check if the result is in the final DP cell
    return result in dp[0][n-1]

s = 0

for result, variables in results_and_variables.items():
    if checkIfPossible(result, variables):
        print("A correct result is: ", result)
        s += result

print("The sum of all correct results is:", s) #Thought wrong this is not working