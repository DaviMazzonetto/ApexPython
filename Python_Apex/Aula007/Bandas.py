# arquivo = open ('bandas.txt', 'a')
# arquivo.write('dejavi;para')
# arquivo.close()


with open('Aulas007/bandas.txt', 'a') as arquivo:
    arquivo.write('dejavu;belém/PA\n')

with open ('Aulas007/bandas.txt' 'r') as arquivo:
    for l in arquivo:
        dados = l.strip().split(';')
        print(f"Nome:{dados[0]} Localização{dados[1]}")
