while True:
    try:
        a = int(input("Ingresa un año: "))
        if a == 0:
            break
        elif a < 0:
            #Si el año es bisiesto es divisible entre 4, pero no divisible entre 100 pero tambien puede ser divisible entre 400
            raise ValueError("Debes ingresar un año positivo")
        elif (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            print(f"Año bisiesto {a}")
        else:
            print(f"Año no bisisesto {a}")
    except ValueError as e:
        print(f"ERROR: {e}")
        