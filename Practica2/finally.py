try:
    numero = int(input("Introduce un numero: "))
except ValueError:
    print("Error: Se ingreso algo que no es un numero entero.")
except ZeroDivisionError:
     print("Error: Estas intentando dividir entre 0")
else:
    resultado = 10 /numero
    print("Resultado:", resultado)
finally: 
    numero1 = int(input("Vamos a hacer una suma, Introduce un numero: "))
    numero2 = int(input("Introduce otro numero: "))
    print(f"Resultado: {numero1 + numero2}")