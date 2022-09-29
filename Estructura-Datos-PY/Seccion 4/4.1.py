from collections import deque

entrada = input().strip().split(" ")
cantidad_vendedores = int(entrada[0])
cantidad_voletas = int(entrada[1])

lista_vendedores = deque()

for i in range(cantidad_vendedores):
    cliente = input().strip().split(" ")
    codigo_cliente = int(cliente[0])
    cantidad_voletas_cliente = int(cliente[1])
    lista_vendedores.append([codigo_cliente, cantidad_voletas_cliente])

contador = 1
while cantidad_voletas > 0 and len(lista_vendedores) > 0:
    cantidad_voletas -= lista_vendedores[0][1]

    if contador == 5:
        lista_vendedores.popleft()
        contador = 1
        if len(lista_vendedores) == 0:
            break

    lista_vendedores.append(lista_vendedores.popleft())

    contador += 1

if cantidad_voletas <= 0:
    mostrar = 0
    if lista_vendedores[0][1] + cantidad_voletas == 0:
        mostrar = lista_vendedores[0][1]
    else:
        mostrar = lista_vendedores[0][1] + cantidad_voletas

    print(lista_vendedores[0][0], mostrar, sep=" ")
else:
    print("quedaron boletas disponibles")