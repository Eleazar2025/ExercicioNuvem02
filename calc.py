# Informações do produto
nome_produto = input("Digite o nome do produto: ") #camiseta
preco_original = input("Digite o preço original: ") #50.00
preco_original = int(preco_original)
percentual_desconto = input("Digite o percentual de desconto em % : ")# 20  %
percentual_desconto = float(percentual_desconto)
# Cálculo do valor de desconto e preço final
valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("Detalhes da Compra")
print("-" * 30)
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
