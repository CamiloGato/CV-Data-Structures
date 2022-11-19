n = int(input())

for i in range(n):
    lista = input().strip().split(" ")
    lista = sorted(list(map(int, lista)))
    suma = 1
    actual = lista[0]
    for j in range(1, len(lista)):  # O(n)
        actual = lista[j - 1]
        if lista[j] == actual:
            suma += 1
        else:
            print(suma, end=" ")
            suma = 1
    print(suma, end="\n")
