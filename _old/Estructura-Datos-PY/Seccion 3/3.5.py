

def bubblesort(elements):
    swapped = False
    pasos = 0
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
                pasos += 1
        if not swapped:
            return pasos
    return pasos


for i in range(int(input())):
    lista = input().strip().split(" ")
    lista = list(map(int, lista))
    print(bubblesort(lista))