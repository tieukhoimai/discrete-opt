## VR505019 - KHOI MAI TIEU
## VR501305 - PEDRO ALONSO LOPEZ TORRES

import sys

def solve(n, arr):
    dp = [-1 for _ in range(n)]
    idx = [[] for _ in range(n)]

    dp[0] = arr[0]
    idx[0] = [0]
    number_of_feasible_solutions = 1 + n

    for i in range(1, n):
        pick = arr[i]

        # Check if there are at least three elements before the current element
        if i > 2:
            pick += dp[i - 3]
            number_of_feasible_solutions += (i - 2)

        non_pick = dp[i - 1]
        
        # Store the maximum of the two choices in the DP table
        dp[i] = max(pick, non_pick)

        if pick > non_pick:
            idx[i].append(i)
            if i > 2:
                idx[i].extend(idx[i - 3])
        else:
            idx[i].extend(idx[i - 1])

    optimal_indices = [i for i, x in enumerate(dp) if x == dp[n-1]]
    optimal_subset = [idx[i] for i in optimal_indices]
    optimal_solution = unique_count = len(set([tuple(sublist) for sublist in optimal_subset]))

    return number_of_feasible_solutions, dp[n - 1], idx[n - 1], optimal_solution

if __name__ == "__main__":
    # Read input file name from command line arguments

	# If no arguments are provided, use the default input file name are conio1/example.in.txt
	if len(sys.argv) == 1:
		input_file_name = './prima_PD_su_linea/example.in.txt'
	# If one argument is provided, use the provided argument as the input file name
	elif len(sys.argv) == 2:
		input_file_name = sys.argv[1]
	else:
		print("Usage: python prima_PD_su_linea-sol.py [input-file-path.txt]")
		sys.exit(1)
	
	output_file_name = input_file_name.replace(".txt", "_output.txt")
	
	# Read the input from input_file_name
	with open(input_file_name, 'r') as file:
		lines = file.readlines()

	# Number of test cases
	T = int(lines[0])

	input_index = 1
	output_lines = []

	for _ in range(T):
		# Read the input for each test case
		# n: number of elements in the array
		n = int(lines[input_index])

		# arr: array of n integers
		input_index += 1
		arr = list(map(int, lines[input_index].split()))

		# Solve the problem
		number_of_feasible_solutions, max_sum, optimal_indices, optimal_solution = solve(n, arr)

		# Prepare the output in the specified format
		output_lines.append(str(number_of_feasible_solutions))
		output_lines.append(str(max_sum))
		output_lines.append(' '.join(map(str, optimal_indices)))
		output_lines.append(str(optimal_solution))

		input_index += 1

	# Write the output to [output_file_name]
	with open(output_file_name, 'w') as file:
		file.write('\n'.join(output_lines))