while True:
    try:
        numero = int(input("Ingresa un numero entero: "))
        if numero < 0:
            raise ValueError("Debes ingresar un número positivo")
        elif numero % 2 == 0:
            print(f"El número es PAR {numero}")
        else:
            print(f"El numero es IMPAR {numero}")
    except ValueError as e:
        print(f"ERROR: {e}")
   