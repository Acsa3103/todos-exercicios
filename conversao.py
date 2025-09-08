num=int(input("Digite um número a ser convertido: \n"))
base=int(input('''escolha a base da conversão: 
para binário digite 1
para octal digite 2
para hexadecimal digite 3
sua escolha: \n'''))
if base==1:
    print("Conversão para binário")
    print("{} convertido para binário é: {}. ".format(num, bin(num)[2:]))
elif base==2:
    print("Conversão para octal")
    print("{} convertido para octal é: {}. ".format(num, oct(num)[2:]))
elif base==3:
    print("Conversão para hexadecimal")
    print("{} convertido para hexadecimal é: {}. ".format(num, hex(num)[2:]))
else:
    print("Escolha inválida, por favor apenas escolha 1, 2 ou 3.")