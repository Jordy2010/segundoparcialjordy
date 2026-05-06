#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio 3:La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula:
# masa = (presión * volumen) / (0.37*(temperatura + 460))
#Fecha de elaboración:16-04-2026

#Solicitar datos al usuario
presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura: "))

#Aplicar la formula
masa = (presion * volumen) / (0.37 * (temperatura + 460))

#Mostrar el resultado
print(f"La masa de aire es: {masa}")
