n = int(input())

for i in range(n):
    tamano = int(input())
    numeros = input().split(" ")
    aux = 0
    puntos = 0
    actual = 0
    while 0 < aux + 1 <= tamano:
        if aux == 0 and puntos != 0:
            puntos += 1
            break

        if numeros[aux] + numeros[actual] == 0:
            puntos += 2
            break

        if int(numeros[aux]) > tamano or int(numeros[actual]) < 0:
            puntos += 1
            break

        actual = int(numeros[aux])
        aux += actual
        puntos += 1

    print(puntos)
