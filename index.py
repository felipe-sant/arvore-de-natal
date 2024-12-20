alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

number = int(input("de 3 até 26: "))
line = ["*"]

print ()

# Testando

if number in range(3,27):
    count = number * 2 - 1
    for x in range(0,number):
        
        # mostra os espaços antes da linha
        print(int(count/2) * " ", end="")

        # troca as iniciais pelo alfabeto
        line[0], line[-1] = alfabeto[x], alfabeto[x]

        # mostra a linha
        for i in line:
            print(i, end="")

        # destroca as iniciais pelo alfabeto
        line[0], line[-1] = "*", "*"

        # adiciona dois * no final da linha
        line.append("*")
        line.append("*")

        # remove 2 do contador
        count -= 2

        print()
else:
    print("numero invalido")

print()