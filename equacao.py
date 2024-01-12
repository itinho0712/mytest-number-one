# Solicita ao usuário os coeficientes da equação
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

# Verifica se 'a' é diferente de zero (não podemos dividir por zero)
if a != 0:
    x = -b/a
    print("A solução da equação é: ", x)
else:
    if b != 0:
        print("A equação não tem solução.")
    else:
        print("A equação tem infinitas soluções.")
