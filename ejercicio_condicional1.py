#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio condicional:1)En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependéra del número de computadoras que compre....
#Fecha de elaboración:22-04-2026

#Función para calcular el descuento en la compra de computadoras
def calcular_descuento(num_computadoras):
    #Precio de cada computadora
    precio_computadoras = 11000
    
    #Condicional para determinaar el descuento según el número de computadoras
    if num_computadoras < 5:
        #Descuento del 10% para menos de 5 computadoras
        descuento =0.1
    elif 5 <= num_computadoras < 10:
        #Descuento del 20% para 5 o más computadoras pero menos de 10
        desceunto = 0.2
    else:
        #Descuento del 40% para 10 o más computadoras
        descuento = 0.4
        
    #Cálculo del total a pagar con descuento
    total = (1 - descuento) * num_computadoras * precio_computadoras
    return total

#Pedir al usuario el número de computadoras
num_computadoras = int(input("Ingrese el número de computadoras: "))
#Inprimir el total a pagar
print("Total a pagar: $", calcular_descuento(num_computadoras))
