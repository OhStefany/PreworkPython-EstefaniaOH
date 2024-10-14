# Ejercicio 18: Contador de Palabras
# Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

def contar_palabras(frase):
  palabras = frase.split()
  print(palabras)
  cantidad_palabras = len(palabras)
  print(cantidad_palabras)
  return cantidad_palabras

oracion = input("Introduce una oracion: ")
numero_palabras = contar_palabras(oracion)
print("La oracion tiene (numero_palabras) palabras.")