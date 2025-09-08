preco = float(input("Qual o valor da casa? "))
sal = float(input("Qual é o seu salário? "))
tempo = int(input("Em quantos anos você vai pagar? "))

mensalidade = (preco / (tempo * 12))
print("Valor da casa: {:.2f}".format(preco))
print("Prestação: {:.2f}".format(mensalidade))

if mensalidade >= (sal * 30 / 100):
    # if sal < (mensalidade * (30 / 100)):
    print("Empréstimo negado.")
else:
    print('''Empréstimo concedido.
    Mensalidade durante {} anos: R${:.2f}.'''.format(tempo, mensalidade))