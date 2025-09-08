s= str(input("Digite M ou F: \n")).strip().upper()[0]
while s not in "MmFf":
    s=str(input("Caro asno, digite M ou F:\n")).strip().upper()[0]
print("sexo do(a) fela é {}".format(s))
print(f"sexo do(a) fela é {s}")