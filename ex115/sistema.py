from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'a1.txt'

if arquivoExiste(arq):
    print('\nArquivo encontrado com sucesso!\n')
else:
    print('\nArquivo não encontrado!\n')
    criarArquivo(arq)

cabecalho('SISTEMA DE ARQUIVO v 1.0')

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # cabecalho('Opção 1')
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)