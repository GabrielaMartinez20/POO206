while True:
    """Escribir un programa que pida al usuario un número entero positivo y muestre 
       por pantalla la cuenta atrás desde ese número hasta cero separados por comas"""
    try:
        num = int(input("Ingresa un número entero positivo ó presiona 0 para salir: "))
        if num == 0:
            break
        elif num < 0:
             raise ValueError("El numero debe ser positivo")
         
        regresiva = []
        for n in range(num, -1, -1):
                regresiva.append(str(n))
        print(", ".join(regresiva))
    except ValueError as e:
        print(f"ERROR: {e}")
            