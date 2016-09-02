Numero = int(input("Número de pessoas:"))
Auxiliar = 0

for i in range(1,Numero + 1):
    Idade = int(input("Idade das pessoas:"))
    Soma = Auxiliar + Idade
    Auxiliar = Soma

Media = Soma / Numero

if (Media >= 0 and Media <= 25):
    print("Turma Jovem!")
elif (Media >= 26 and Media <= 60):
    print("Turma Adulta!")
elif (Media > 60):
    print("Turma Idosa!")
