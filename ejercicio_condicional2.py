#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio condicional 2:2)
#Fecha de elaboración:23-04-2026

#Función para calcular el precio de las llantas según la promoción
def calcular_precio_llantas(num_llantas):
    #Condicional para determinar el precio de cada llanta
    if num_llantas < 5:
        #Precio de $300 por llanta para menos de 5 llantas
        precio_llanta = 300
    elif 5 <= num_llantas <=10:
        #Precio de 4250 por llanta para 5 o más llantas pero no más de 10
        precio_llanta = 250
    else:
        #Precio de $200 por llanta para más de 10 llantas
        precio_llanta = 200
        
    #Cálculo del total a pagar
    total = num_llantas * precio_llanta
    return total

#Pedir al usuario el número de llantas
num_llantas = int(input("Ingrese el número de llantas"))
#Inprimir el total a pagar
print("Total a pagar: $", calcular_precio_llantas(num_llantas))
