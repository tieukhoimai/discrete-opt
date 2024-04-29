# VR505019 - KHOI MAI TIEU
# VR501305 - PEDRO ALONSO LOPEZ TORRES

#!/usr/bin/env python3
from sys import stderr, stdout, argv

MOD = 10**9 + 7

def solve(n,out_nei):
    # TODO: write here your solution!
    # what follows will be just good enough to respect the intended communication protocol with the server

    # Lista distanze dei nodi a partire da 0
    dist = [n+1] * n

    # Lista dei padri di ciascun nodo
    dad = [-1] * n              # Inizializzo a -1 i padri perché con il while continuo a ciclare finché non trovo tutti i padri
                                # N.B.: potrebbe esserci il caso in cui un nodo non sia raggiungibile (non ha un padre)
                                # questo significa che il programma va in loop infinito

    # Numero di possibili alberi BFS minimi
    num_BFStrees = 1            # È inizializzato a 1 perché verrà moltiplicato per il numero di combinazioni

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Altre variabili/strutture dati utili

    possibili_padri = []        # Lista di possibili padri per un nodo i-esimo
                                # len(possibili_padri) = numero combinazioni per il nodo i-esimo

    nodi_valutati = []          # Lista di liste dei nodi da valutare per ciascuna iterazione

    nodi_next = []              # Lista di liste che si costruisce a ogni iterazione per i nodi successivi da valutare
                                # a fine di ogni iterazione: nodi_valutati = list(nodi_next)
    
    costo = 0                   # Numero di ramificazioni (costo per arrivare a un nodo i-esimo)


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # TASK 1: ricavare il costo minimo per ogni nodo (dist)
    # TASK 2: assegnare i padri per ciascun nodo (dad)
    # TASK 3: calcolare tutte le combinazioni di BFS trees minimi (num_BFStrees)

    dist[0] = 0                           # Il nodo 0 ha come distanza 0
    dad[0] = 0                            # Il nodo 0 ha come padre sé stesso

    for i in range(1,n):        # Valuto ogni nodo con un for 1,...,n-1
        costo = 1               # Il costo per tutti i nodi (eccetto lo 0) è inizializzato a 1
        nodi_next = []
        nodi_valutati = [list(out_nei[0])]    # I primi nodi che valuto sono quelli del nodo padre

        # Inseriamo direttamente i figli del nodo 0
        if i in out_nei[0]:
            dad[i] = 0
            dist[i] = costo
            continue

        visitati = [0]           # Lista dei nodi che visito per andare a trovare i
        while -1 in dad:                   # Itero finché non trovo tutti i dad (in dad non ci sono -1)
            
            for lista in nodi_valutati:    # In lista sono presenti i figli di ciascun nodo
                                           # in caso di i = 0 -> [2, 5, 3]  |  [3, 6, 9], [6, 4, 9], [5, 8]
                for nodo in lista:         # nodo = 2, 5, 3  |  3x, 6, 9, 6x, 4, 9x, 5x, 
                    
                    # Se il nodo è stato già visitato in passato, allora non lo visita
                    if nodo in visitati:
                        continue
                    else:
                        visitati.append(nodo)   # Se il nodo è nuovo, allora lo visito

                    # Il nodo i-esimo è tra i figli di nodo
                    if i in out_nei[nodo]:
                        possibili_padri.append(nodo)        # [6, 4, 8]

                        # Aggiorno il costo minimo del nodo i-esimo
                        if dist[i] == n+1:
                            costo += 1
                            dist[i] = costo         # i = 1 -> costo = 3
                    else:
                        nodi_next += [list(out_nei[nodo])]        # [[8], ] = nodi_next
                
                #
            # Finiti i nodi_valutati da valutare, se ci sono dei possibili padri abbiamo finito per il nodo i-esimo
            if len(possibili_padri) > 0:
                num_BFStrees *= len(possibili_padri)        # Aggiorno il numero delle possibilità con i possibili padri
                dad[i] = possibili_padri[0]                 # Il padre del nodo i-esimo è il primo dei possibili padri
                possibili_padri = []                        # Azzero la lista dei possibili padri
                break
            costo += 1
            nodi_valutati = list(nodi_next)     # [[3, 6, 9], [6, 4, 9], [5, 8]]
            nodi_next = []
            
    return dist, dad, num_BFStrees % MOD

              
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
