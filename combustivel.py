# Dados da viagem
distancia_percorrida = input("Digite distância percorrida: ") #300  # em km
combustivel_gasto = input("Digite a quantidade de combustível gast0: ") #25      # em litros
distancia_percorrida = float(distancia_percorrida)
combustivel_gasto = float(combustivel_gasto)
# Cálculo do consumo médio (km/l)
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("Relatório de Consumo de Combustível")
print("-" * 40)
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
