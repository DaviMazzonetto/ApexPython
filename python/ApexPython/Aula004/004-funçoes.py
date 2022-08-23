def mensagem():
    print('Olá')


def soma(n1,n2): # Parametros
    soma = n1 + n2
    print(soma)

def soma2(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma

def soma3(n1,n2,n3=0,n4=0): # parametro opcional
    print('n1:',n1, 'n2:',n2, 'n3:',n3, 'n4:',n4)
    return n1 + n2 + n3 + n4

mensagem()
soma(33,44) # argumentos

r = soma2(33, 44, 77)
print(r)

f = soma3(44, 154)
print(f)

r = soma3(n2= 10, n1=20) # argumentos nomeados
print(r)