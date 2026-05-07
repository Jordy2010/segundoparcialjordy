#Nombre del alumno:Jordy Eduardo Sebastian Lopez
#Ejercicio While:1
#Fecha de elaboración:24-04-2026

n = int(input("Ingrese el número de vendedores: "))
i = 0
while i < n:
    sueldo = float(input("Ingrese el sueldo base: "))
    venta1 = float(input("Ingrese la venta 1: "))
    venta2 = float(input("Ingrese la venta 2: "))
    venta3 = float(input("Ingrese la venta 3: "))
    comision = (venta1 + venta2 + venta3) * 0.1
    total = sueldo + comision
    print("Comision: ", comision)
    print("Total: ", total)
    i += 1
