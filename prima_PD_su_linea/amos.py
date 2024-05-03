#!/usr/bin/env python3
from sys import stderr, stdout, argv

MOD = 10**9 + 7

supporto = {
    0: 1,
    1: 2,
    2: 3,
    3: 4
}

def num_feasible_solutions(n):
    """returns the number of feasible solutions for an input array A of n cells."""
    assert n >= 0
    # TODO: write here your solution! 
    # what follows will be just good enough to respect the intended communication protocol with the server
    # @Pedro

    if n in supporto:
        return supporto[n] % MOD

    tot = n + 1

    # sum_{i=1}^{n-3} i = casi(casi + 1) / 2
    casi = n - 3
    somma = int((casi * (casi + 1)) / 2)

    tot += somma

    # trovo i sottoproblemi j
    j = 4
    cont = 1
    while (j * 2) - cont <= n:
        tot += solve(j) - (j + 1)
        j += 1
        cont += 1

    if n not in supporto:
        supporto[n] = tot % MOD

    return supporto[n]

def solve(n, arr):
    dp = [-1 for _ in range(n)]
    idx = [[] for _ in range(n)]

    dp[0] = arr[0]
    idx[0] = [0]

    for i in range(1, n):
        pick = arr[i]

        # Check if there are at least three elements before the current element
        if i > 2:
            pick += dp[i - 3]

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

    return dp[n - 1], idx[n - 1], optimal_solution

def optimize(n,A):
    """returns the triple (optval,optsol,num_optsols) where optsol is the list of indexes of any optimal solution for the instance comprising of the first n cells of array A. A first inefficient but essential solution might take inspiration from a minimal recursive implementation of the function num_feasible_solutions above"""
    assert n >= 0
    assert n == len(A)
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server

    num_optsols = 1 % MOD

    dp = [-1 for _ in range(n)]
    idx = [[] for _ in range(n)]

    dp[0] = A[0]
    idx[0] = [0]

    for i in range(1, n):
        pick = A[i]

        # Check if there are at least three elements before the current element
        if i > 2:
            pick += dp[i - 3]

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
    num_optsols = len(set([tuple(sublist) for sublist in optimal_subset]))

    return dp[n - 1], idx[n - 1] ,num_optsols
              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n = int(input())
        if debug_level > 1:
            print(f"{n=}", file=stderr)
        A = list(map(int, input().strip().split()))
        if debug_level > 1:
            print(f"{A=}", file=stderr)
        optval, optsol, num_optsols = optimize(n,A)
        num_feas_sols = num_feasible_solutions(n)
        if debug_level > 2:
            print(f"{num_optsols=},{optval=},{optsol=},{num_feas_sols=}", flush=True, file=stderr)
        fouts = [stderr, stdout] if debug_level > 3 else [stdout]
        for fout in fouts:
            print(num_feas_sols, file=fout)
            print(optval, file=fout)
            print(" ".join(map(str,optsol)), file=fout)
            print(num_optsols, file=fout)
            fout.flush()
