def verificar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")  
    elif edad < 18:
        raise ValueError("Debes ser mayor de edad.")
    else:
        print("¡Acceso permitido!")

try:
    edad = int(input("Ingresa tu edad: "))
    verificar_edad(edad)
except ValueError as e:
    print(f"Error: {e}")