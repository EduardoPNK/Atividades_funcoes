#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(n1, n2, n3):
    resultado = n1 + n2 + n3
    return resultado

numero1 = int(input('Informe um numero para soma: '))
numero2 = int(input('Informe um numero para soma: '))
numero3 = int(input('Informe um numero para soma: '))

print(f'a soma é {soma(numero1, numero2, numero3)}')