Numero = int(input("Montar a tabuada de:"))
Inicio = int(input("Começar por:"))
Fim = int(input("Terminar em:"))
Mult = 0

if(Inicio < Fim):
    print("Vou montar a tabuada de",Numero,"começando em",Inicio,"e terminando em",Fim)
    while(Inicio <= Fim):
        Mult = Inicio * Numero
        print(Numero,"x",Inicio,"=",Mult)
        Inicio = Inicio + 1
else:
    print("O número inicial é maior que o número final")
