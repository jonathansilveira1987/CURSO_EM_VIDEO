# Gerenciador de Pagamentos.

print("{:=^60}".format(" Lojas Silveira "))
compra = float(input("\nInforme o valor da compra: "))
print('''\nEscolha a forma de pagamento:
[ 1 ] - Dinheiro.
[ 2 ] - Cheque.
[ 3 ] - À vista no Cartão de Crédito.
[ 4 ] - 2 x Cartão de Crédito.
[ 5 ] - 3 x ou mais no cartão de Crédito.\n''')
pagamento = int(input("Escolha a forma de pagamento: "))
if pagamento == 1:
    dinheiro = compra - (compra * 10 / 100)
    print("\nVocê recebeu desconto de 10% em sua compra.")
    print("O valor à pagar é de R$ {:.2f}.\n".format(dinheiro))
if pagamento == 2:
    cheque = compra - (compra * 10 / 100)
    print("\nVocê recebeu desconto de 10% em sua compra.")
    print("O valor à pagar é de R$ {:.2f}.\n".format(cheque))
if pagamento == 3:
    cartao = compra - (compra * 5 / 100)
    print("\nVocê recebeu 5% de desconto em sua compra.")
    print("O valor à pagar é de R$ {:.2f}.\n".format(cartao))
if pagamento == 4:
    print("\nO valor à pagar é de R$ {:.2f}.\n".format(compra))
if pagamento == 5:
    parcelado = compra + (compra * 20 / 100)
    print("\nSua compra tem acréscimo de 20% de juros.")
    print("O valor à pagar é de R$ {:.2f}.\n".format(parcelado))