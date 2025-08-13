### 📊 Análisis de Ventas en Python

Este proyecto realiza un análisis básico de ventas utilizando estructuras de datos en Python. A partir de una lista de transacciones, se calcula información clave como ingresos totales, productos más vendidos y precios promedio, y se genera un resumen exportable en formatos `.txt` y `.csv`.

#### 📁 Estructura del Script

El archivo principal contiene las siguientes secciones:

1. **Carga de Datos**  
   Se define una lista de diccionarios con ventas simuladas, incluyendo fecha, producto, cantidad y precio unitario.

2. **Cálculo de Ingresos Totales**  
   Se calcula el total de ingresos sumando el producto de cantidad y precio por cada venta.

3. **Análisis del Producto Más Vendido**  
   Se identifica el producto con mayor cantidad total vendida.

4. **Promedio de Precio por Producto**  
   Se calcula el precio promedio ponderado por unidad para cada producto.

5. **Ventas por Día**  
   Se agrupan los ingresos por fecha para obtener una visión diaria de las ventas.

6. **Resumen de Ventas por Producto**  
   Se genera un diccionario anidado con:
   - Cantidad total vendida  
   - Ingresos totales  
   - Precio promedio

7. **Exportación de Resultados**  
   Se guardan los resultados en:
   - `resumen_ventas.txt`: resumen legible en texto plano  
   - `resumen_ventas.csv`: archivo estructurado para análisis externo

#### 📦 bibliotecas

Este script utiliza únicamente bibliotecas estándar de Python.


🧠 Autor
Ale2jandro


