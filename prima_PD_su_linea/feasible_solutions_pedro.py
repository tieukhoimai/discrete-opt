def count_feasible_solutions(arr, n):
    feasible_solutions = 0

    if n == 0:
         pass
    
    elif n == 1 or n == 2 or n == 3:
        feasible_solutions += n + 1   

    else:
        # n = 4 --> 6 feasible solutions
        # n = 6 --> 13 feasible solutions
        for idx_1 in range(0, len(arr)):
            for idx_2 in range(idx_1, len(arr), 3):
                if idx_2 - idx_1 >= 3:
                    for idx_3 in range(0, (len(arr) - idx_2) + 1):
                        feasible_solutions += 1
                elif idx_2 < len(arr):
                    feasible_solutions += 1
        feasible_solutions += 1                     # adding the empty set
                
            
    return feasible_solutions

print(count_feasible_solutions([1, 2, 3, 4, 5], 5))