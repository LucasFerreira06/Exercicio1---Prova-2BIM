QtdTemp = int(input("Quantidade de temperaturas:"))
Temp = int(input("Digite a temperatura:"))
Maior = Temp
Menor = Temp
Soma = 0
Auxiliar = 1

while(Auxiliar <= QtdTemp):
    if(Auxiliar < QtdTemp):
        Temp = int(input("Digite a temperatura:"))
    if(Temp > Maior):
        Maior = Temp
    elif(Temp < Menor):
        Menor = Temp
    Soma = Soma + Temp
    Auxiliar = Auxiliar + 1
print("A Maior temperatura será:",Maior,"graus")
print("A Menor temperatura será:",Menor,"graus")
Media = Soma / QtdTemp
print("A média das temperaturas será:",Media,"graus")


