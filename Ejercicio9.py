# Ejercicio 9: Conversor de Divisas
# Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.

def dolares_a_euros(dolares):
  euros = dolares * 0.85
  return euros

cantidad_dolares = float(input("Introduce la cantidad de dolares: "))
cantidad_euros = dolares_a_euros(cantidad_dolares)

print(f"La cantidad convertida a euros es: {cantidad_euros}")
