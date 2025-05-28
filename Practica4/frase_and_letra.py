while True:
    """3. Escribir un programa en el que se pregunte al usuario por una frase y una letra,
        y muestre por pantalla el número de veces que aparece la letra en la frase."""
    try: 
        frase = input("Ingresa una frase: ").lower()
        if frase == "0":
            break
        l = input("Ingresa una letra: ").lower()
        if l == "0":
            break
        count = frase.count(l)
        print(f"La letra {l} aparece {count} veces en la frase")
    except Exception as e:
        print(f"ERROR: {e} ")
                