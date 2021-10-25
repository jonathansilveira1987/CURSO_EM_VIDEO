aluno = (input("Digite o nome do aluno(a): "))
idade = int(input("Digite a idade do aluno(a): "))

if idade < 1:
    print("Digite uma idade válida.")
if idade > 1 or idade <= 5:
    print(f"O aluno(a) {aluno} tem {idade} anos e está na Educação Infantil.".format(aluno, idade))
elif idade >= 6 or idade <= 10:
    print(f"O aluno(a) {aluno} tem {idade} anos e está no Ensino Fundamental I.".format(aluno, idade))
elif idade >= 11 or idade <= 14:
    print(f"O aluno(a) {aluno} tem {idade} anos e está no Ensino Fundamental II.".format(aluno, idade))
else:
    print(f"O aluno(a) {aluno} tem {idade} anos e está no Ensino Médio.".format(aluno, idade))