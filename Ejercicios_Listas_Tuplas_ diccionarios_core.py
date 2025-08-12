#1 Carga de Datos:
#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
# «producto»: una cadena de texto que represente el nombre del producto vendido.
# «cantidad»: un número entero que represente la cantidad de productos vendidos.
# «precio»: un número flotante que represente el precio unitario del producto.

import numpy as np
ventas= [
    {"fecha": "2024-01-01", "producto": "fideos", "cantidad": 3, "precio": 1500.6},
    {"fecha": "2024-01-02", "producto": "Salsa de tomate", "cantidad": 5, "precio": 500.5},
    {"fecha": "2024-01-03", "producto": "queso rallado", "cantidad": 4, "precio": 950.3},
    {"fecha": "2024-01-04", "producto": "carne molida", "cantidad": 3, "precio": 300.25}
]

#2 Cálculo de Ingresos Totales:
#Utiliza un bucle para iterar sobre la lista ventas y
#  calcular los ingresos totales generados por todas las ventas. 
# Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

ingresos_totales = 0
for venta in ventas : 
    ingresos_totales += venta["precio"]* venta["cantidad"]
    print(f"Ingresos totales : ${ ingresos_totales:.2f}")

#3 Análisis del Producto Más Vendido:
# Crea un diccionario llamado ventas_por_producto
#  donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
# Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

ventas_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad


producto_mayor_vendida = max(ventas_por_producto, key=ventas_por_producto.get)

print("Ventas por producto:", ventas_por_producto)
print(f"El producto más vendido es '{producto_mayor_vendida}' con {ventas_por_producto[producto_mayor_vendida]} unidades.")

#4 Promedio de Precio por Producto.
# Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas.
#Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

precios_por_producto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio_total = cantidad * venta["precio"]  

    if producto in precios_por_producto:
        precios_por_producto[producto] = (precios_por_producto[producto][0] + precio_total, precios_por_producto[producto][1] + cantidad)
    else:
        precios_por_producto[producto] = (precio_total, cantidad)

promedio_por_producto = {producto: precio_total / cantidad_total for producto, (precio_total, cantidad_total) in precios_por_producto.items()}

print("Precios acumulados por producto:", precios_por_producto)
print("Promedio de precio por producto:", promedio_por_producto)

#5 Ventas por Día:
#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

ingresos_por_dia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"] 

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

        print("Ingresos por día:", ingresos_por_dia)

#6 Representación de Datos:
#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados.
#Cada diccionario anidado debe contener:
#«cantidad_total»: la cantidad total vendida del producto.
#«ingresos_totales»: los ingresos totales generados por la venta del producto.
#«precio_promedio»: el precio promedio de venta del producto.

resumen_ventas = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ingresos = cantidad * venta["precio"]

    if producto in resumen_ventas:
        resumen_ventas[producto]["cantidad_total"] += cantidad
        resumen_ventas[producto]["ingresos_totales"] += ingresos
    else:
        resumen_ventas[producto] = {"cantidad_total": cantidad, "ingresos_totales": ingresos}

for producto, datos in resumen_ventas.items():
    datos["precio_promedio"] = datos["ingresos_totales"] / datos["cantidad_total"]

print("Resumen de ventas:", resumen_ventas) 


#guardar 
with open("resumen_ventas.txt", "w") as archivo:
    archivo.write("Lista de Ventas Original:\n")
    for venta in ventas:
        archivo.write(f"{venta}\n")

    archivo.write("\nIngresos Totales:\n")
    archivo.write(f"${ingresos_totales:.2f}\n")

    archivo.write("\nProducto Más Vendido:\n")
    archivo.write(f"{producto_mayor_vendida} con {ventas_por_producto[producto_mayor_vendida]} unidades\n")

    archivo.write("\nPrecio Promedio por Producto:\n")
    for producto, precio_promedio in promedio_por_producto.items():
        archivo.write(f"{producto}: ${precio_promedio:.2f}\n")

    archivo.write("\nIngresos Totales por Día:\n")
    for fecha, ingreso in ingresos_por_dia.items():
        archivo.write(f"{fecha}: ${ingreso:.2f}\n")

    archivo.write("\nResumen de Ventas por Producto:\n")
    for producto, datos in resumen_ventas.items():
        archivo.write(f"{producto}: {datos}\n")

print("Resultados guardados en 'resumen_ventas.txt'")

#guardar csv 
import csv

with open("resumen_ventas.csv", "w", newline="") as archivo_csv:
    escritor = csv.writer(archivo_csv)

    # Escribir encabezados
    escritor.writerow(["Producto", "Cantidad Total Vendida", "Ingresos Totales", "Precio Promedio"])

    # Escribir datos
    for producto, datos in resumen_ventas.items():
        escritor.writerow([producto, datos["cantidad_total"], datos["ingresos_totales"], datos["precio_promedio"]])

print("Resultados guardados en 'resumen_ventas.csv'")



















































