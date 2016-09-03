Numero = int(input("Digite um número:"))
Fatorial = 1
Ext = Numero

while(Numero > 1):
    Fatorial = Fatorial * Numero
    Numero = Numero - 1
print("Fatorial de:",Ext)

for a in range(1,Ext + 1):
    print(Ext)
    print("x")
    Ext = Ext - 1
print("=",Fatorial)
