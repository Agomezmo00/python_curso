#print ('Hola, estamos en la sesión 1 de Python')

saludo = 'Hola, estamos en la sesión 1 de Python'

#print(type(saludo))
#print(saludo)

saludo = 90
#print(type(saludo))

nombre = "Antonio"
#saludo = "Hola, me llamo "+nombre
 
""" la f al inicio de la cadena le aplica el formato, 
para que no te saque {nombre} sino el valor de la variable """

anyos = 36
saludo = f"Hola, me llamo {nombre} y tengo {anyos} años"

#print(saludo)


#Si la longitud del nombre es mayor que 7 y es mayor de edad entonces....
if anyos >= 18 and len(nombre) >= 7:
    print("La condición es correcta")
else:
    print("La condición no es correcta")

condicion = anyos >= 18
print(type(condicion))
print(anyos)

a = 10
b = 30

if len(nombre) == 7:
    print("7 caracteres")
else:
    print("no 7 caracteres")