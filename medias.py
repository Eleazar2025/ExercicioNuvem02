# Notas do aluno
nota1 = input("Digite a nota 1: ") #7.5
nota2 = input("Digite a nota 2: ") #8.0
nota3 = input("Digite a nota 3: ") #6.5
nota1 = float(nota1)
nota2 = float(nota2)
nota3= float(nota3)

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição dos resultados
print("Boletim do Aluno")
print("-" * 25)
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média final: {media:.2f}")
