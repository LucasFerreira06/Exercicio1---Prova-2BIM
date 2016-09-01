Numero = int(input("Digite um número:"))
A = 2

while(A <= Numero):
    if(Numero % A == 0):
        print("O número",Numero,"não é um número primo")
        break
    else:
        (Numero % A == 1)
        print("O número",Numero,"é um número primo pois ele é divisível por 1 e ele mesmo")
        break
