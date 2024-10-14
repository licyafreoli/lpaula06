capital = float(input("digite sua capital inicial:"))
juros = float(input("digite sua capital atual:"))
tempo = float(input("tempo:"))

juros = juros/100
valor = capital * juros * tempo

print(f"seu juros simples é {valor}")
