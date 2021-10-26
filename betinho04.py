from random import seed
from random import randint

listas = [[]] # Uma lista de lista.


while True:
    print('''
            - MENU -

    [ 1 ] - Nova Inscrição
    [ 2 ] - Visualizar Inscrição
    [ 0 ] - Encerrar
    ''')
    op = int(input()) # Escolha da opção.

    if op == 1:
            id = () # cria uma lista para adicionar o nome, e-mail, telefone e curso.
            nome = input("Digite o nome da pessoa: ")
            email = input("E-mail: ")
            telefone = input("Telefone com DDD: ")
            curso = input("Curso: ")
            id.append(nome)
            id.append(email)
            id.append(telefone)
            id.append(curso)
            # listas(id) #Adiciona a lista criada com o cadastro da pessoa dentro da lista.

    elif op == 2:
            for mostrar in listas:
                for mostrar2 in mostrar:
                    print(mostrar2) # mostra tudo dentro da opção.

    elif op == 0:
        print("Encerrado!")
    break

print(id)