from time import sleep

print('''
            - MENU -

    [ 1 ] - Nova Inscrição
    [ 2 ] - Visualizar Inscrição
    [ 3 ] - Encerrar
    ''')

opcao = 0
while opcao != 3:

    opcao = int(input("Qual sua opção? "))

    if opcao == 1:
        nome = str(input("\nDigite seu nome: "))
        email = str(input("Digite seu e-mail: "))
        telefone = int(input("Digite seu telefone com DDD: "))
        curso = str(input("Digite seu Curso: "))
    elif opcao == 2:
        print('-=' * 20)
        print('----------    FICHA DE CADASTRO    ----------')
        print(nome)
        print(email)
        print(telefone)
        print(curso)
        print('-=' * 20)
    elif opcao == 3:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente Novamente.")
    print("-=" * 10)
    sleep(2)    
print("Fim do Programa! Volte Sempre!")



