# Sistema interativo de ajuda em Python.


c = ('  \033[m'         # 0 - sem cores
     '  \033[0;30;41m', # 1 - vermelho
     )

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')

# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP.', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)




