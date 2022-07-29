def calculadora(n1, n2, op):
    if op=="1":
        return n1 + n2
    elif op=="2":
        return n1 - n2
    elif op=="3":
        return n1 * n2
    elif op=="4":
        return n1 / n2
    else:
        return 0


n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))

op = input("ESCOLHA A OPERAÇÃO DESEJADA: \n"
    "1. SOMA \n"
    "2. SUBTRAÇÃO \n"
    "3. MULTIPLICAÇÃO \n"
    "4. DIVISÃO \n"
    "--->  ")

print(calculadora(n1, n2, op))
