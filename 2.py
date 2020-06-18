#Faça um programa para imprimir:
#    1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def repeticoes(usuario):
    for linha in range(1, usuario+1):
        for coluna in range(1, linha + 1):
            print(coluna, end=' ')
        print("")

vezes = int(input('Informe o valor para a contagem: '))

repeticoes(vezes)