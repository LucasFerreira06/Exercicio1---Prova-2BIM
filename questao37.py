Altura = eval(input("Digite a Altura:"))
TotalAlt = 0
TotalPeso = 0
MaiorPeso = 0
MenorPeso = 0
MaiorAlt = 0
MenorAlt = 0
AuxiliarAlt = 1
AuxiliarPeso = 1

while (Altura != 0):
    TotalAlt = TotalAlt + Altura
    if (Altura > MaiorAlt):
        MaiorAlt = MaiorAlt + Altura
    else:
        MenorAlt = MenorAlt + Altura
    Altura = eval(input("Digita a Altura:"))
    MediaAlt = TotalAlt / AuxiliarAlt
    AuxiliarAlt = AuxiliarAlt + 1
    
Peso = eval(input("Digite o Peso:"))
    
while (Peso != 0):
    TotalPeso = TotalPeso + Peso
    if (Peso > MaiorPeso):
        MaiorPeso = MaiorPeso + Peso
    else:
        MenorPeso = MenorPeso + Peso
    Peso = eval(input("Digite o Peso:"))
    MediaPeso = TotalPeso / AuxiliarPeso
    AuxiliarPeso = AuxiliarPeso + 1
    
print("Mais Gordo:",MaiorPeso)
print("Mais Magro: ",MenorPeso)
print("Mais Alto: ",MaiorAlt)
print("Mais Baixo: ",MenorAlt)
print("Média dos Pesos: ",MediaPeso)
print("Média das Alturas: ",MediaAlt)
