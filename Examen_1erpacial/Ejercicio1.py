while True:
    try:
        n = int(input("Ingresa un numero entre 200 y 400: "))
        if n == 0:
            break
        elif n < 0:
            raise ValueError("Ingresa un numero dentro del rango")
        elif n >= 200 and n <= 400:
            par = []
            for num in range(n,402):
                if num % 2 == 0:
                    print(f"{num},")
        else:
            print("Ingresa un numero dentro del rango")
    except Exception as e:
        print(f"ERROR: {e}")
        