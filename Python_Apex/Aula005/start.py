from calculadora import soma, subt, mult, div


print('='*10, 'Calculadora Apex','='*10)
print('''
    1 -Soma
    2- Subtração
    3- Multiplicação
    4- Divisão
    ''')
resposta = int(input('Digite uma opção:'))

n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))
n4 = int(input('Digite o quarto número:'))

resultado = 0

if (resposta == 1):
    print('Soma')
    resultado = soma(n1,n2,n3,n4)
elif(resposta == 2):
    print('Subtração')
    resultado = subt(n1,n2,n3,n4)
elif(resposta == 3):
    print('Multiplicação')
    resultado = mult(n1,n2,n3,n4)
elif(resposta == 4):
    print('Divisão')
    resultado = div(n1,n2,n3,n4)
else:
    print('Opção inválida')

print('Resultado da conta:', resultado)



