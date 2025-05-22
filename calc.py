# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20  # em %

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
