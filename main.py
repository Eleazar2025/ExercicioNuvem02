# Valores fornecidos
valor_reais = 100.00  # Valor em reais
taxa_dolar = 5.20     # Cotação do dólar
taxa_euro = 6.15      # Cotação do euro

# Conversão dos valores
valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

# Exibição formatada com duas casas decimais
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Convertido em dólares: US$ {valor_em_dolar:.2f}")
print(f"Convertido em euros: € {valor_em_euro:.2f}")
