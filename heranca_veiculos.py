# Classe base (Pai)
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"


# Classe derivada (Filha)
class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        # Usa o construtor da classe Pai
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def exibir_informacoes(self):
        # Reaproveita o método da classe Pai e adiciona informação extra
        info_pai = super().exibir_informacoes()
        return f"{info_pai} | Número de portas: {self.numero_portas}"


# Programa principal (para testar)
print("=== Cadastro de Veículo ===")

marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
portas = int(input("Digite o número de portas: "))

carro1 = Carro(marca, modelo, portas)

print("\nInformações do veículo:")
print(carro1.exibir_informacoes())
