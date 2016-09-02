Notas = int(input("Digite a quantidade de notas:"))
Nota = eval(input("Digite uma nota:"))
Auxiliar = 0

while(Auxiliar < Notas):
    Soma = Nota + Nota
    Auxiliar = Auxiliar + 1
    if (Auxiliar < Notas):
        Nota = eval(input("Digite uma nota:"))
Media = Soma / Notas
print("A média é:",Media) 
