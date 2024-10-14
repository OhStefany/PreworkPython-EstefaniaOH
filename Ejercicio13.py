# Ejercicio 13: Verificación de Número Primo
# Escribe un programa que determine si un número ingresado por el usuario es primo o no.

def es_primo(numero):
  if numero <= 1:
    return False
  for 1 in range(2, numero):
    if numero %1 ==0:
      return False
  return True

numero = int(input("Introduce un numero: "))

if es_primo(numero):
  print(f"El numero {numero} es primo!")
else:
  print(f"El numero {numero} no es primo!")