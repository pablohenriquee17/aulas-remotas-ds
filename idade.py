#Pergunte o nome do usuário e guarde na variável 'nome'
nome = input("Qual é o seu nome? ")

#Pergunte a idade e guarde na variável 'idade_texto'
idade_texto = input("Qual é a sua idade? ")

#Converta a idade de texto para número
idade_numero = int(idade_texto)

#Crie a lógica condicional
if idade_numero >= 18:
    # Complete com a mensagem para maior de idade
    # Exemplo: Olá, [Nome], você é maior de idade.
    print(f"Olá, {nome}, você é maior de idade.")
else:
    # Complete com a mensagem para menor de idade
    # Exemplo: Olá, [Nome], você é menor de idade.
    print(f"Olá, {nome}, você é menor de idade.")