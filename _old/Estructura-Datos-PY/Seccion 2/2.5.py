n = input()
texto = []

for i in range(3):
    texto.append(input().split(", "))

puntos1 = 0
puntos2 = 0
puntos3 = 0
for i in range(int(n)):
    sum = 0

    for j in range(3):
        sum += int(texto[j][i])

    if sum%2 == int(texto[0][i])%2:
        puntos1 += 1
    if sum%2 == int(texto[1][i])%2:
        puntos2 += 1
    if sum%2 == int(texto[2][i])%2:
        puntos3 += 1

print(f"SO:{puntos1}, LAR:{puntos2}, IS:{puntos3}")
