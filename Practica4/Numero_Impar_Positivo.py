while True:
    """Escribir un programa que pida al usuario un número entero positivo mayor de 10 y
       que muestre como resultado todos los números impares desde 2 hasta ese número
       separados por comas."""
    try:
        num = int(input("Ingresa un número entero positivo mayor de 10 ó presiona 0 para salir: "))
        if num == 0:
            break
        elif num <= 10:
            raise ValueError("El numero debe ser mayor que 10")
        impar = []
        for n in range(2,num + 1):
                if n % 2 != 0:
                    impar.append(str(n))
                    
        print(", ".join(impar))
    except ValueError as e:
        print(f"ERROR: {e}")
                