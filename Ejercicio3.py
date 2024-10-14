# Ejercicio 3: Verificación de Edad
# Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad (mayor o igual a 18 años) o no.

def verificar_edad(edad):
  if edad>0:
   if edad>= 18:
    return "Eres mayor de edad"
   else:
    return "Eres menor de edad"
  else:
    return "Edad incorrecta"

edad = int(input("Introduce tu edad: "))
mensaje = verificar_edad(edad)
print(mensaje)
  