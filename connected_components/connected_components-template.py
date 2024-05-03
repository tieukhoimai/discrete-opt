## VR505019 - KHOI MAI TIEU
## VR501305 - PEDRO ALONSO LOPEZ TORRES

#!/usr/bin/env python3
from sys import stderr, stdout, argv


MOD = 10**9 + 7

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if not visited[i]:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = [False] * self.V
        cc = []
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

def solve(n, nei):
    # Create a graph instance
    graph = Graph(n)
    
    # Add edges to the graph based on the 'nei' parameter
    for v, neighbours in enumerate(nei):
        for neighbour in neighbours:
            graph.addEdge(v, neighbour)
    
    # Retrieve connected components using the graph's method
    connected_components = graph.connectedComponents()
    
    return connected_components

if __name__ == "__main__":
    debug_level = 0
    if len(argv) == 2:
        debug_level = int(argv[1])
    T = int(input())
    for t in range(1, 1 + T):
        if debug_level > 0:
            print(f"#\n# Testcase {t}:", file=stderr)
        n, m = map(int, input().strip().split())
        nei = [ [] for _ in range(n) ]
        for _ in range(m):
            a, b = map(int, input().strip().split())
            nei[a].append(b)
            nei[b].append(a)
        if debug_level > 1:
            print(f"# {n=}, {m=}, {nei=}", file=stderr)
        CC = solve(n,nei)
        if debug_level > 2:
            print(f"# {CC=}", flush=True, file=stderr)
        print(len(CC))
        for C in CC:
            print(" ".join(str(v) for v in C))
