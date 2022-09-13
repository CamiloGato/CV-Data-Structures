n = int(input())

for i in range(n):
    numeros = input().strip()
    numeros = numeros.split(" ")
    numeros = sorted(list(map(int, numeros)))

    k = int(input())
    for i in range(k):
        dos = input().strip().split(" ")
        distancia = abs(numeros.index(int(dos[0])) - numeros.index(int(dos[1])))
        print(f"{distancia} kms")
