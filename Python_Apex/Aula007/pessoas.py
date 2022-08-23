def salvar (nome):
    with open('Aulas007/pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('Aulas007/pessoas.txt', 'r') as arquivo: # nomeia tudo aulo de arquivpo
        for l in arquivo: # para cada lomja de arquivp
            l = l.strip() # retira espaçoo ers quebras de linhas do começo e final da string
            nomes.append(l)
    return nomes

salvar ('luiza Helena')
print (listar())