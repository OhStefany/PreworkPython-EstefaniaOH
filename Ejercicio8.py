# Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
# Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona, utilixando la formua \( IMC = \frac{peso}{altura^2} \).

def calcular_imc(peso, altura):
  imc = peso / (altura **2)
  return imc

peso = float(input("Introduce tu peaso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu indice de Masa Corporal es: {imc:.2f}")