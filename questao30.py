Preço = eval(input("Digite o preço do pão R$:"))
print("Preço do pão R$:",Preço)
print("Panificadora Pão de Ontem - Tabela de preços")
Auxiliar = 1

for Tabela in range(0,50):
    print(Auxiliar,"- R$ %.2f" %(Preço * Auxiliar))
    Auxiliar = Auxiliar + 1
    
