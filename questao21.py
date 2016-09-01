Numero = int(input("Digite um número:"))
A = 2

while(A <= Numero):
    if(Numero % A == 0):
        print("O número",Numero,"não é um número primo")
        break
    else:
        print("O número",Numero,"é um número primo")
        break
    

