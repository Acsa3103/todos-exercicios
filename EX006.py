def preco(produto1, produto2, produto3):
    media = (produto1 + produto2 + produto3)
    if media >= 1000:
        return "barato"
    else:
        return "caro pra carai"
produto1 = float(input("digite o primeiro preço: "))
produto2 = float(input("digite o segundo preço: "))
produto3 = float(input("digite o terceiro preço: "))
resultado = preco(produto1, produto2, produto3)
print(f"O produto está {resultado}.")
