def soma(a,b):
    soma = a+b
    return soma

def subtracao(a,b):
    subtracao= a-b
    return subtracao

a = float(input("Digite o núumero:"))
b = float(input("Digite  núumero:"))

RSoma= soma(a,b)
RSub= subtracao(a,b)

print(f"A soma é igual ao número: {RSoma}")
print(f"A subtraçção é igual a: {RSub}")


