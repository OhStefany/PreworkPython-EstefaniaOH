# Ejercicio 1: Conversor de Temperatura
#Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
#La formula es: F = C * (9/5)

def celsis_a_farenheit(celsius):
  return celsius * (9/5) + 32

temperatura_celsius= float (input ("Introducta la temperatura a convertir a Grados Faranheit"))

Temperatura_faranheit = celsis_a_farenheit (temperatura_celsius)

print("La temperatura en Faranheint es: (Temperatura_faranheit)")