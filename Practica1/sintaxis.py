#1. COMENTARIOS
#comentarios de una sola linea

"""
comentario de mas de 1 linea 
en python """

#2. Strings
print('soy la otra')

variable1 =  "hola soy una cadena"
print(len(variable1))
print(variable1[2:5])
print(variable1[2:])
print(variable1[:5])

#3. VARIABLES
x = "gabi"
x = 4
x = 5.90
print(x)

x = int(3)
y = float(3)
z = str(3)

print(x,y,z)
#Por si se olvida el tipo de dato que le coreesponde
print(type(x))
print(type(y))
print(type(z))

#4. Solicitud de datos
a = input("Introduce cualquier dato: ")
b = int(input("Introduce un numero entero: "))
c = float(input("Introduce un numero decimal: "))
print(a,b,c)

#5. boolean,comparacion y logicos
print(10 > 9)
print(10 < 9)
print(10 == 9)
print(10 >= 9)
print(10 <= 9)
print(10 != 9)

x = 1
print(x<5 and x < 10)
print(x<5 or x < 10)
print(not(x<5 and x < 10))