try:
    numero = int(input("Introduce un numero: "))
    resultado = 10 /numero
    print(f"Resultado:{resultado}")
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")