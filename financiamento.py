import time

casa = float(input("Qual e o valor da casa que você quer comprar?"))
salario = float(input("Quantos você recebe?"))
salario = salario * (30 / 100)

anos_pagando= float(input('Em quantos anos você vai parcelar?'))
parcelas = casa / (anos_pagando * 12)

print("processando informações...")
time.sleep(3)

print(f"Suas parcelas serão de R${parcelas:.2f}")

if parcelas <= salario:
  print("Parabès algem vai sair de casa nova hoje!")
elif parcelas > salario:
  print("Infelizmente, o financiamento não foi aprovado. AS parcelas ultrapassam 30% do seu salário.")
else:
  print("Alguma coisa deu errado. Verifique os valores informados")