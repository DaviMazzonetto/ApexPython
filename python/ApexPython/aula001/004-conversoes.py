cabecalho = '-'*10
print(cabecalho,'Sistemas de cadastro de produtos',cabecalho)

nome = input('Digite o nome do produto:')
descricao = input('Digite a descrição do produto:')
valor = input('Digite o valor do produto')
quantidade = input('Digite a quantidade do produto')
perecivel = input('Perecivel?(S/N)')

print('O produto', nome,'-',descricao, 'de valor: R$',valor,    
        'e quantidade', quantidade,'(perecível:',perecivel,')', 
        '\nfoi cadastrado com sucesso!')
