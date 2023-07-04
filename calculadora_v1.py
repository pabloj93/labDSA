# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Calculadora simples em Python! É possível fazer contas de adição (+), subtração (-), multiplicação (*) e divisão (/).")

def soma(a,b):
    return a+b

def multiplicacao(a,b):
    return a*b

def subtracao(a,b):
    return a-b

def divisao(a,b):
    if b == 0:
        print("Não é possível dividir por zero!!!")
        b = float(input("Digite um divisor diferente de zero:"))
    return a/b

parcial = float(input("Digite o primeiro número da conta:"))

conta = input("Digite o tipo de conta que quer fazer (+|-|*|/):")

while conta != "=":
    b = float(input("Digite o próximo número da conta:"))
    if conta == "+":
        parcial = soma(parcial, b)
        print("O resultado parcial é %s"%(parcial))
    elif conta == "-":
        parcial = subtracao(parcial, b)
        print("O resultado parcial é %s"%(parcial))
    elif conta == "*":
        parcial = multiplicacao(parcial, b)
        print("O resultado parcial é %s"%(parcial))
    elif conta == "/":
        parcial = divisao(parcial, b)
        print("O resultado parcial é %s"%(parcial))
    else: print ("Tipo de conta inexistente.")
    
    conta = input("Digite o tipo de conta que quer fazer (+|-|*|/) ou = para obter o resultado final:")

total = parcial
print("O resultado final é %s"%(total))

    

