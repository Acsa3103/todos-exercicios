import math
print("vamos calcular nossas vendas!")
quantidade_pizzas_vendidas_=int(input("quantas pizzas ja vendidas?"))
valor_venda_pizza=float(input("qual valor de venda de cada pizza:R$"))
custo_pizza=float(input("qual o custo de producao R$"))
liquido=valor_venda_pizza-custo_pizza
print(f"o valor de lucro é de: R${liquido:.2f}")
meta_finaceira_liquida=float(input("qual a meta de lucro desejada?"))

if liquido<=0:
    print("\n erro: valor preco errado")
    print("ajuste os valores novamente")
else:
    lucro_acumulado=quantidade_pizzas_vendidas_*liquido
    lucro_faltante=meta_finaceira_liquida-lucro_acumulado
    print("\n em resumo teremos:")
    if lucro_faltante<=0:
        print(f"meta atingida, parabéns! Chegamos a R$ {meta_finaceira_liquida:.2f}. ")
        print(f"lucro liquido acumulado: R$ {lucro_acumulado:.2f}")
    else:
        pizza_para_vender=lucro_faltante/liquido
        pizzas_necessarias=math.ceil(pizza_para_vender)
        print(f"Para meta falta R$ {meta_finaceira_liquida:.2f}")
        print(f"você precisa vender {pizzas_necessarias}pizzas")
        print(f"O lucro liquido é R$ {lucro_acumulado:.2f}")
        print(f"lucro liquido faltante R$ {lucro_faltante:.2f}")
            