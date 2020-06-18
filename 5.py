#Faça um programa com uma função chamada somaImposto.
#A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
#que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    resultado = custo * (1 + (taxaImposto/100))
    return resultado

imposto = float(input('Informe a taxa de imposto em %: '))
valor = float(input('Informe o valor inicial do item: '))
print(somaImposto(imposto, valor))