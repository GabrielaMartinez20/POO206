while True:
    try:
        palabra = str(input("Ingresa una palabra o 0 para salir: "))
        if palabra == "0":
            break 
        #elif palabra > "0" and palabra < "0":
        #   raise ValueError("Ingresa un numero dentro del rango")
        else:
            i=1 #declaro la variable que se va incrementar
            for l in palabra:
                print (f"Letra {i}: {l}") #Agrego la variable "i" que va a contar las letras
                i= i+1 #Se tiene que incrementar para hacer que cambie el numero en cada ciclo.
    except Exception as e:
        print (f"ERROR: {e}")