QtdNumeros = int(input("Digite a quantidade de números que você quer comparar:"))
Numero = int(input("Digite um número:"))
Maior = Numero
Menor = Numero
Soma = 0
Auxiliar = 1
for a in range(Auxiliar,QtdNumeros):
    if (Auxiliar < QtdNumeros):
        Numero = int(input("Digite um número:"))
    if (Numero > Maior):
        Maior = Numero
    elif (Numero < Menor):
        Menor = Numero
    Soma = Maior + Menor 
    Auxiliar = Auxiliar + 1
    
print("Maior número é:",Maior)
print("Menor número é:",Menor)
print("Soma igual a:",Soma)
