#!/usr/bin/env python3
from sys import stderr, stdout, argv


MOD = 10**9 + 7

'''
out_nei contiene le uscite dei singoli nodi

0: [2,3]
1: [0,2]
2: [1]
3: [1]
'''
# Task 1 -> contare le distanze tra i nodi a partire dal nodo 0
#           d(0,0), d(0,1), d(0,2), ... , d(0,n-1)
def fun_task1(n, out_nei):
    dist = [0] * n
    for i in range(1, n):                       # i: nodo di destinazione a partire dal nodo 0
        dist_temp = [n] * len(out_nei[0])       # le distanze delle possibili strade verso il nodo di destinazione a partire da 0
        for idx, j in enumerate(out_nei[0]):    # j: nodi collegati al nodo 0
            d_temp = 1                          # distanza temporanea da 0 al nodo di destinazione
            next = list(out_nei[j])
            while j != i:
                if i in out_nei[j]:
                    d_temp += 1
                    break
                j = next[0]
                next = next[1:]
                next += out_nei[j]
                d_temp += 1
            dist_temp[idx] = d_temp
        dist[i] = min(dist_temp)
    return dist


# Task 2 -> analizziamo il grafo con BFS
#           N.B.: nella task 1 è stata utilizzata una pseudo-DFS
def fun_task2(n,out_nei):
    dad = [-1] * n
    dad[0] = 0
    initial_node = 0
    next_nodes = list(out_nei[initial_node]) # 2,4
    while -1 in dad:
        for i in out_nei[initial_node]:
            if dad[i] == -1:
                dad[i] = initial_node   # 0 -1 0 2 0 2
                next_nodes += out_nei[i]      # [2 4 3 5 2 5 1 1]
        initial_node = next_nodes[0]          # 2 , 4
        next_nodes = next_nodes[1:]                 # [3 5 2 5 1 1]
    return dad


def solve(n, out_nei):
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server
    num_BFStrees = (n - 2) % MOD  # -> numero archi albero - 1

    # Task 1
    dist = fun_task1(n,out_nei)

    # Task 2
    dad = fun_task2(n,out_nei)
    

    return dist, dad, num_BFStrees

              
if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        out_nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b = map(int, input().strip().split())
            out_nei[a].append(b)
        if debug_level > 1:
            print(f"# {n=}, {m=}, {out_nei=}", file=stderr)
        dist, dad, num_BFStrees = solve(n,out_nei)
        if debug_level > 2:
            print(f"# {num_BFStrees=}\n# {dist=}\n# {num_BFStrees=}", flush=True, file=stderr)
        print(" ".join(map(str,dist)))
        print(" ".join(map(str,dad)))
        print(num_BFStrees)
