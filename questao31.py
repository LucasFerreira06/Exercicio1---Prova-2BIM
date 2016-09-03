Valor = eval(input("Digite o valor do produto:"))
ValorTot = 0

while(Valor != 0):
    ValorTot = ValorTot + Valor
    Valor = eval(input("Digite o valor do produto:"))
print("Valor Total =",ValorTot)

Dinheiro = eval(input("Digite o valor do dinheiro:"))
Troco = Dinheiro - ValorTot
print("O valor do troco será de",Troco,"R$")
