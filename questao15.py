Numero = int(input("Digite o n-ésimo número:"))
W = 1
X = 1
Y = 0
Auxiliar = 1

print(X)
print(X)

while(Auxiliar <= Numero - 2):
    Y = W + X
    print(Y)
    Auxiliar = Auxiliar + 1 
    W = X
    X = Y
print("Fim da série") 
