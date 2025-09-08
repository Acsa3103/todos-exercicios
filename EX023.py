s = 0
for num in range(1, 501):  # de 1 até 501
    if num % 2 != 0:  # Ímpares
        if num % 3 == 0:  # Ímpares múltiplos de 3
            s += num  # soma = soma + num
print("A soma dos múltiplos é: {}.".format(s))

#o código calcula a soma de todos os números entre 1 e 501 que são ímpares e múltiplos de 3.