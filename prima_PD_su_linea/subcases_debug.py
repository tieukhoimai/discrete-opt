def finding_subcases(lista, n):

    subcases = []                                               
    indici_lista = list(range(0, len(lista)))
    
    # In questo modo inludo i casi generici in cui ogni elemento si trova
    # ad una distanza di 3 dall'altro
    for idx_1 in range(0, len(lista)):
        numero_elementi = []                         
        for idx_2 in range(idx_1, indici_lista[-1], 3):
            numero_elementi.append(idx_2)  
        if len(numero_elementi) >= 3:
            subcases.append(numero_elementi)

    for idx_1 in range(0, len(lista)):
        numero_elementi = []                         
        for idx_2 in range(idx_1, indici_lista[-1], 3):
            numero_elementi.append(idx_2)
            if indici_lista[-1] - idx_2 <= 3:
                for idx_3 in range(indici_lista[-1], idx_2, -1):
                    for idx_4 in range(idx_2 - 3, 0, -3):
                        numero_elementi.apped(idx_4)
                    numero_elementi.append(idx_3)
            subcases.append(numero_elementi)

    return subcases

lista_prova = [9, 3, 4, 5, 7, 3, 6, 5, 5]
