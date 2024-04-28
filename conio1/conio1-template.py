#!/usr/bin/env python3
from sys import stderr, stdout, argv

pieces = [1,2,5,10,20,50,100,200,500,1000]

def solve(total):
    # TODO: write here your solution!
    denominations = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    coins, remaining = sorted(denominations, reverse=True), total
    pieces_used = [0] * len(denominations)

    for i, coin in enumerate(coins):
        coins_used = remaining // coin
        pieces_used[i] = coins_used
        remaining -= coins_used * coin

    total_pieces = sum(pieces_used)

    return total_pieces, reversed(pieces_used)

if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        S = int(input())
        if debug_level > 0:
            print(f"#\n# Testcase {t} ({S=}):", file=stderr)
        optval, optsol = solve(S)
        if debug_level > 1:
            print(f"# {optval=}\n# {optsol=}", flush=True, file=stderr)
        print(optval)
        print(" ".join(map(str,optsol)))
