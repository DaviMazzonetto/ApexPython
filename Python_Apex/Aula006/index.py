arquivo = open('Aula006/pessoas.txt', 'a') # Abre um arquivo no formato de escrita, colocando o conteudo no final do arquivo
arquivo.write('Davi\n') # Insere um texoto com quebra de linha
arquivo.close() # Fecha o arquivo


arquivo = open('Aula006/Pessoa.txt', 'r') # Abre no formato de leitura
for linha in arquivo:
    print(linha) # Print contém quebra de linha
    linha = linha.strip() # Retira espaços e quebras de linha do começo e final da string
arquivo.close() 




