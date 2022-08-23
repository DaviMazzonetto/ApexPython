# Criação e leitura de Arquivos
# w= abre em modo de escrita
# se o arquivo não existir cria, se existir substitui

arquivo = open('nomes.txt','w' ) 
arquivo.write('LMGSS')
arquivo.close()

# x= abre em modo de escita
# se o arquivo não existir cira, se existir substitui

arquivo = open('numeros.txt','x' ) 
arquivo.write('10')
arquivo.close()
 
#  a= abre em modo de escrita,
#  se o arquivo nao existir, cira, mas se existir, adiciona dados ao final
arquivo = open('bandas.txt','a' ) 
arquivo.write('Death')
arquivo.close()
 

