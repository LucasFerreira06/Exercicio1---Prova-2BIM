Eleitores = int(input("Digite a quantidade eleitores:"))
Candidato1 = 0
Candidato2 = 0
Candidato3 = 0

for a in range(1,Eleitores + 1):
    Votos = int(input("Digite os votos:"))
    if(Votos == 1):
        Candidato1 = Candidato1 + 1
    elif(Votos == 2):
        Candidato2 = Candidato2 + 1
    elif(Votos == 3):
        Candidato3 = Candidato3 + 1
    else:
        while(Votos != 1 and Votos != 2 and Votos != 3):
            print("Voto inválido, digite novamente")
            Votos = int(input("Digite os votos:"))

print("O candidato 1 obteve",Candidato1,"votos!")
print("O candidato 2 obteve",Candidato2,"votos!")
print("O candidato 3 obteve",Candidato3,"votos!")


        
