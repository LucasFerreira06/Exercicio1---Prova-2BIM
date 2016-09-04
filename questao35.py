Numero = int(input("Digite um número:"))
Auxiliar = 0
A = 2
B = 1
for a in range(A,Numero):
    while (B <= A):
        if ((A % B) == 0):
            Auxiliar = Auxiliar + 1
        B = B + 1
    if(Auxiliar == 2):
        print(A)
    B = 1
    A = A + 1
    Auxiliar = 0
