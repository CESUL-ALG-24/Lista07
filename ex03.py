populacao = int(input("Informe a população atual da cidade: "))
taxa = float(input("Informe a taxa de crescimento anual: "))

for _ in range(15):
    populacao = populacao * (1 + taxa/100)

print(f"A população da cidade, após 15 anos será de {populacao:.0f}")
