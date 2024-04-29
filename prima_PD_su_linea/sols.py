def maxSum(arr, n):
	# Base case
	if n == 0:
		return 0
	if n == 1:
		return arr[0]
	if n == 2:
		return max(arr[0], arr[1])

	# DP table to store solutions to subproblems
	dp = [0] * n

	# Initializing base cases
	dp[0] = arr[0]
	dp[1] = max(arr[0], arr[1])

	# Filling up the DP table using recurrence relation
	for i in range(2, n):
		dp[i] = max(dp[i - 1], arr[i] + dp[i - 3])

	# Returning the final answer
	return dp[n - 1]

if __name__ == "__main__":
    # Input array
    arr = [1,2,3,4,5,6]
    n = len(arr)
    print(maxSum(arr, n))

def count_feasible_solutions(arr, n):
    feasible_solutions = 0
    if n == 0:
        return feasible_solutions
    elif n == 1 or n == 2 or n == 3:
        feasible_solutions += 1
        return feasible_solutions
    else:
        # n = 4 --> 6 feasible solutions
        # n = 5 --> 13 feasible solutions
        # per vedere se due oggetti sono adiacenti o hanno un oggetto adiacente in comune
        # si può calcolare la differenza dei loro indici
        # nel caso sia uguale a 1 o 2, allora non possono venire selezionati
        for idx_1, object in enumerate(arr):
                for idx_2 in range(idx_1, len(arr), 3):
                    feasible_solutions += 1
                    idx_2 += 3
                    if idx_2 <= len(arr):
                        feasible_solutions += 1
            
        return feasible_solutions


                           
                    
            
                  



	
		
