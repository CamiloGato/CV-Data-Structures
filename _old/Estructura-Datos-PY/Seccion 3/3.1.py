def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return (mid + 1)

    # If we reach here, then the element was not present
    return 0


lon_lista = int(input())
lista = list(map(int, input().strip().split(" ")))

lon_elementos = int(input())
elementos = list(map(int, input().strip().split(" ")))

suma = 0

for elemento in elementos:

    suma += binary_search(lista, elemento)

print(suma)
