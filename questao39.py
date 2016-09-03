Numero = eval(input("Digite o número do aluno:"))
Altura = eval(input("Digite a altura do aluno:"))
Maior = Altura
Menor = Altura
NumMaior = 0
NumMenor = 0

for a in range(1,11):
    if(Altura > Maior):
        Maior = Altura
        NumMaior = Numero
    elif(Altura < Menor):
        Menor = Altura
        NumMenor = Numero

    if(a != 10):
        Numero = eval(input("Digite o número do aluno:"))
        Altura = eval(input("Digite a altura do aluno:"))

print("Número do maior aluno:",NumMaior,"- Altura do maior aluno:",Maior,"centímetros")
print("Número do menor aluno:",NumMenor,"- Altura do menor aluno:",Menor,"centímetros")
        
