#Faça um programa, com uma função que necessite de um argumento.
#A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def validacao(numero):
    if numero < 0:
        print('N')
    elif numero > 0:
        print('P')
    else:
        print('Nulo')

validar = int(input('Informe um numero para validação: '))

validacao(validar)