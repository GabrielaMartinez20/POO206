import re

while True:
    print("Requisitos de contraseña:\n"
          "Debe contener como mínimo 10 caracteres\n"
          "Debe contener al menos un número\n"
          "Debe contener al menos un carácter especial")
    
    contraseña = input("Ingresa una contraseña o 'salir' para terminar: ").strip()
    
    if contraseña.lower() == 'salir':
        print("Adios")
        break

    errores = 0
    
    if len(contraseña) < 10:
        print("Contraseña demasiado corta")
        errores += 1
    
    if not any(c.isdigit() for c in contraseña):
        print("Debe contener al menos un número")
        errores += 1
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
        print("Debe contener al menos un carácter especial")
        errores += 1
    
    if errores >= 1:
        print("\nPor favor revisa los requisitos e intenta nuevamente.\n")
    else:
        print("\n¡Contraseña válida!")
        break