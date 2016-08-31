Vezes = int(input("Quantidade de vezes do cáculo vetorial:"))
Numero = int(input("Digite um número:"))
Fatorial = 1

for x in range(Vezes):
    if(Numero < 16):
        for a in range(1,Numero):
            Fatorial = Fatorial * Numero
            Numero = Numero - 1

        print(Fatorial)

    else:
        print("Valor não suportado")

    
    Fatorial = 1
    if(x < (Vezes - 1)):
        Numero = int(input("Digite um número:"))

    
        
