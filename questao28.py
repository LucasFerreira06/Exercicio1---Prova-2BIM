CDS = int(input("Digite a quantidade de CDS:"))
Soma = 0

for i in range(1,CDS + 1):
    Valor = eval(input("Digite o valor de cada CD:"))
    Soma = Soma + Valor

Media = Soma / CDS
print("Valor gasto em cada CD:",Media)
print("Valor gasto em toda a coleção:",Soma)
    
