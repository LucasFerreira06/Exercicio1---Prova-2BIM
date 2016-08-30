Numero = int(input("Digite um número:"))
Quantidade = 0
Pares = 0
Impares = 0

while(Quantidade <= 9):
    if (Numero % 2 == 0):
        Pares = Pares + 1
    else:
        Impares = Impares + 1
    if (Quantidade < 9):
        Numero = int(input("Digite um número:"))
    Quantidade = Quantidade + 1
print("A quantidade de números pares são:",Pares)
print("A quantidade de números ímpares são:",Impares)
