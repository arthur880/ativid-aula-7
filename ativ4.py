n1 = float (input("digite a nota 1:"))
n2 = float (input("digite a nota 2:"))
n3 = float (input("digite a nota 3:"))
n4 = float (input("digite a nota 4:"))

media = (n1+n2+n3+n4)/4
if media >= 6:      
    print(f"voce foi aprovado{media}")
else:
    print(f"voce foi reprovado{media}")