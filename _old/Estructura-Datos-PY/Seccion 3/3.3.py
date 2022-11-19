import math


# function save divisors of n in a list
def divisors(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n):

        if n % i == 0:

            # If divisors are equal, print only one
            if n / i == i:
                divisors.append(i)
            else:
                # Otherwise print both
                divisors.append(i)
                divisors.append(int(n / i))
        i = i + 1
    return divisors


def primoConjunto(n, lista):
    div = divisors(n)
    for d in div:
        if str(d) not in lista:
            return False
    return True


n = input()
for i in range(int(n)):
    [cantidad, numero] = input().strip().split(" ")
    numeros = input().strip().split(" ")
    divisores = divisors(int(numero))
    if primoConjunto(int(numero), numeros):
        print("Es PrimiConjunto")
    else:
        print("No es PrimiConjunto")
