def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid + 1

    return 0


lon_lista = int(input())
lista = list(map(int, input().split(" ")))

lon_elementos = int(input())
elementos = list(map(int, input().split(" ")))


suma = 0

for i in range(lon_elementos):

    suma += binary_search(lista, elementos[i])

print(suma)
