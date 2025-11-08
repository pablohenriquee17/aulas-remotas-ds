def calculadora(numero1, numero2, operacao):
    """
    Função que realiza uma operação matemática básica entre dois números.
    """
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 == 0:
            return "Erro: divisão por zero"
        return numero1 / numero2
    else:
        return "Operação inválida"


# Programa principal
print("=== Calculadora Simples ===")

# Entrada de dados do usuário
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

# Chamada da função
resultado = calculadora(n1, n2, op)

# Saída
print("Resultado:", resultado)
