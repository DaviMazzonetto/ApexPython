arquivo = open ('Aula006/produtos.txt', 'a') # Abre um arquivo no formato de escrita, colocando o conteudo no final do arquivo
arquivo.write('Cerveja;IPA;R$24.00\n') # Formato CSV, colunas
arquivo.close() # fecha o arquivo

arquivo.open('Aula006/produtos.txt','r')
for linha in arquivo:
    linha = linha.strip() # Retira espaços e quebras de linha do começo e final da string
    dados = linha.split(';') # forma uma lista, cria um elemento para cada caracter encontrado
    print(f'Nome: {dados[0]} Tipo: {dados[1]} Valor: {dados[2]}') # fstrings, interpolação de string
arquivo.close()

arquivo.open('Aula006/produtos.txt','r')
for linha in arquivo:
    dados = linha.strip().split(';')
    print(f'Nome: {dados[0]} Tipo: {dados[1]} Valor: {dados[2]}') 
arquivo.close()