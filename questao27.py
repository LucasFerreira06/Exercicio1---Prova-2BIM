Turmas = int(input("Digite a quantidade de turmas existentes:"))
Soma = 0

for x in range(1,Turmas + 1):
    Alunos = int(input("Digite a quantidade de alunos existentes:"))

    if(Alunos <= 40):
        Soma = Soma + Alunos
    else:
        print("Excedeu o número máximo de alunos (40)")

Media = Soma / Turmas
print("Quantidade média de alunos por turma:",Media)
