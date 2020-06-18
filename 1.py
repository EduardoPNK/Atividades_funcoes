#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def repetição(usuario):
    for n in range(1,usuario + 1):
        print(f'{n} '* n)

informacao = int(input('Informe um número: '))

repetição(informacao)