#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio 1:Dada un cantidad en pesos, obtener la equivalencia en dólares,asumiendo que la unidad cambiara es un dato desconocido
#Fecha de elaboración:16-04-2026

#Solicitar los datos al usuario

pesos = float(input("Ingrese la cantidad en pesos: "))
tipo_cambio = float(input("Ingrese el valor del tipo de cambio (1 dólar = ? pesos): "))
#Realizar la conversión
dolares = pesos / tipo_cambio

#Mostrar el resultado
print(f"La equivalencia es: {dolares:.2f} dólares")
