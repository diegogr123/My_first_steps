# Ejercicio:
# Pide al usuario que ingrese 3 números, guárdalos en una lista y muestra la suma total de esos números.
#

numero1 = int(input("ingresa un numero: "))
numero2 = int(input("ingresa otro numero: "))
numero3 = int(input("ingresa un numero más: "))

listanum = [numero1, numero2, numero3]

suma = sum(listanum)

print (f"la suma es igual a: {suma}")