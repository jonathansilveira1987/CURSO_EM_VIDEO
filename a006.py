listas = [[]] #uma lista de lista

while True:
    print('''
            - MENU -

    [ 1 ] - Nova Inscrição
    [ 2 ] - Visualizar Inscrição
    [ 0 ] - Encerrar
    ''')
    op = int(input())#Escolha da opcao
    if op == 1:
        nova = [] # cria uma lista para adicionar o id, nome e idade da pessoa
        id = input("Id da pessoa")
        nome = input("Digite o nome da pessoa")
        idade = input("Idade da pessoa")
        nova.append(id)
        nova.append(nome)
        nova.append(idade)
        listas.append(nova)#Adiciona a lista criada com o cadastro da pessoa dentro da lista

    elif op == 2:
        for mostrar in listas:
            for mostrar2 in mostrar:
                print(mostrar2)#mostra tudo dentro da

    elif op == 0:
        print("Encerrado!")
    break