n1 = int(input("Digite um lado do triângulo: "))
n2 = int(input("Digite o segundo lado do triângulo: "))
n3 = int(input("Digite o terceiro lado do triângulo: "))
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("Os lados informados formam um triângulo.")
else:
    print("Os lados informados não formam um triângulo.")