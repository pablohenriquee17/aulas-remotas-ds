#Peça ao usuário um número e converta-o para inteiro
numero_str = input("Digite um número para ver a tabuada: ")
numero = int(numero_str)

print(f"--- Tabuada do {numero} ---")

#Crie um loop 'for' que vá de 1 até 10
#A variável 'i' vai assumir o valor de 1, depois 2, depois 3... até 10
for i in range(1, 11):
    # 3. Calcule o resultado da multiplicação
    resultado = numero * i

    # 4. Imprima o resultado formatado
    # (Use f-strings para formatar a saída)
    # Exemplo: 7 x 1 = 7
    print(f"{numero} x {i} = {resultado}")