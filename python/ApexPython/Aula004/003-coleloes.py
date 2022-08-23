lista = ['Davi', 'Luiza','Lua']
tupla = (10,20,30) # Imutável = somente leitura
dicionario = {'nome': 'Davi', 'idade':20, 'salario':2040.00}

print(lista[2])
print(tupla[0])
print(dicionario['idade'])

lista[2] = 'Mel'
# tupla[2] = 12 # erro, não pode ser alterada
dicionario['salario'] = 3
dicionario['endereco'] = 'Belém do Pará' # dicionario cria novo valor caso nao tenha criado
print(dicionario)


