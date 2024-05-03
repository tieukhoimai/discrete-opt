## VR505019 - KHOI MAI TIEU
## VR501305 - PEDRO ALONSO LOPEZ TORRES

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
        tot += num_feasible_solutions(j) - (j + 1)
        j += 1
        cont += 1

    if n not in supporto:
        supporto[n] = tot % MOD

    return supporto[n]


def optimize(n, A):
    """returns the triple (optval,optsol,num_optsols) where optsol is the list of indexes of any optimal solution for the instance comprising of the first n cells of array A. A first inefficient but essential solution might take inspiration from a minimal recursive implementation of the function num_feasible_solutions above"""
    assert n >= 0
    assert n == len(A)

    dp = [-1 for _ in range(n+1)]
    idx = [[] for _ in range(n)]
    num_optsols = [0 for _ in range(n+1)]

    dp[0] = A[0]
    num_optsols[0] = 1

    for i in range(1, n+1):
        pick = A[i-1]
        
        # Check if there are at least three elements before the current element
        if i > 3:
            pick += dp[i - 3]
            num_optsols_if_pick = num_optsols[i - 3]
        else:
            num_optsols_if_pick = 1

        non_pick = dp[i - 1]
        num_optsols_if_not_pick = num_optsols[i - 1] 
                
        # Store the maximum of the two choices in the DP table
        dp[i] = max(pick, non_pick)

        if pick > non_pick:
            idx[i-1].append(i-1)
            num_optsols[i] = num_optsols_if_pick % MOD
            if i > 2:
                idx[i-1].extend(idx[i - 4])
        elif pick < non_pick:
            idx[i-1].extend(idx[i-2])
            num_optsols[i] = num_optsols_if_not_pick % MOD
        else:
            num_optsols[i] = (num_optsols_if_pick + num_optsols_if_not_pick) % MOD

    return dp[n], idx[n-1], num_optsols[n]

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