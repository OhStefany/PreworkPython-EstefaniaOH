# Ejercicio 14: Calculadora de Descuento
#Crea un programa que calcule el precio final de un artículo después de aplicar un descuento del 20%.

def calcular_precio_total(precio):
  descuento =precio * 0.2
  total = precio + descuento
  return total

precio_original = float(input("Introduzca el precio del articulo: "))

precio_descuento = calcular_precio_total(precio_original)

print(f"El total a pagar, incluyendo el descuento es: {precio_descuento}")
