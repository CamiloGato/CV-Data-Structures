for i in range(int(input())):
    lista = input().strip()
    lista = lista.split(", ")
    lista = list(map(int, lista))
    lista.sort()
    ind = 0
    ini = len(lista) - 1
    si = 0
    sd = 0
    izquierda = []
    derecha = []
    while True:

        if si < sd:
            izquierda.append(lista[ini])
            si += lista[ini]
            ini -= 1
        else:
            derecha.append(lista[ind])
            sd += lista[ind]
            ind += 1

        if ind == ini:
            if si < sd:
                izquierda.append(lista[ini])
            else:
                derecha.append(lista[ind])
            break


    print( abs(sum(izquierda) - sum(derecha)) )