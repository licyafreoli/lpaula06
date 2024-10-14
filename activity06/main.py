valor= (float(input("qual o preço original do produto?")))
original= (float(input("digite sem % a porcentagem do desconto:")))

desc = original/100
final= desc * valor
print (f"o valor final do produto com desconto é {final}")
