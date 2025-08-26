# Ejercicio:
# Pide al usuario un número y dile si es par o impar.
#
# Pistas:
# - Un número es par si al dividirlo entre 2 el residuo es 0.
# - Usa el operador % (módulo) para comprobarlo.
# - Muestra un mensaje indicando si el número es par o impar.
numero = int(input("Rápido, escribe un número: "))
divisor = 2

if numero % divisor == 0:
    print(f"{numero}, es par")
else:
    print(f"{numero}, es impar")