## VR505019 - KHOI MAI TIEU
## VR501305 - PEDRO ALONSO LOPEZ TORRES

from sys import stderr, stdout, argv

MOD = 10**9 + 7

def optimize(n,A,C):
    assert n >= 0
    assert n == len(A)
    assert n == len(C)

    num_feas_sols = 2
    dp = [A[i] for i in range(n)]
    idx = [[i] for i in range(n)]
    feas_dp = [[1] for _ in range(n)]
    optsols = [[1] for _ in range(n)]
    
    max_val = dp[0]
    num_optsols = optsols[0][0]
    optsol = idx[0]

    for i in range(1, n):
        for j in range(i):
            if i - j > C[i] + C[j]:
                feas_dp[i][0] = (feas_dp[i][0] + feas_dp[j][0]) % MOD
                if dp[j] + A[i] > dp[i]:
                    dp[i] = dp[j] + A[i]
                    optsols[i][0] = optsols[j][0]
                    idx[i] = idx[j] + [i]
                elif dp[j] + A[i] == dp[i]:
                    optsols[i][0] = (optsols[i][0] + optsols[j][0]) % MOD
                    if idx[j] + [i] not in idx[i]:
                        idx[i] = idx[j] + [i]
        num_feas_sols = (num_feas_sols + feas_dp[i][0]) % MOD

        if dp[i] > max_val:
            max_val = dp[i]
            optsol = idx[i]
            num_optsols = optsols[i][0]
        elif dp[i] == max_val:
            num_optsols = (num_optsols + optsols[i][0]) % MOD

    if max_val == 0:
        num_optsols = 1

    return num_feas_sols, max_val, optsol, num_optsols

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
        C = list(map(int, input().strip().split()))
        if debug_level > 1:
            print(f"{C=}", file=stderr)
        num_feas_sols, optval, optsol, num_optsols = optimize(n,A,C)
        if debug_level > 2:
            print(f"{num_optsols=},{optval=},{optsol=},{num_feas_sols=}", flush=True, file=stderr)
        fouts = [stderr, stdout] if debug_level > 3 else [stdout]
        for fout in fouts:
            print(num_feas_sols, file=fout)
            print(optval, file=fout)
            print(" ".join(map(str,optsol)), file=fout)
            print(num_optsols, file=fout)
            fout.flush()