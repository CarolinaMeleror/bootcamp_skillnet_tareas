# 1. Carga de Datos
# Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta.
# Cada venta debe incluir las siguientes claves:
# «fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
# «producto»: una cadena de texto que represente el nombre del producto vendido.
# «cantidad»: un número entero que represente la cantidad de productos vendidos.
# «precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {"fecha": "2024-01-11", "producto": "Harina",
     "cantidad": 10, "precio": 2200.000},
    {"fecha": "2024-01-15", "producto": "Azucar",
     "cantidad": 10, "precio": 15.000},
    {"fecha": "2024-02-20", "producto": "Crema",
     "cantidad": 5, "precio": 30.000},
    {"fecha": "2024-02-11", "producto": "Harina",
     "cantidad": 3, "precio": 120.000},
    {"fecha": "2024-03-17", "producto": "Azucar",
     "cantidad": 2, "precio": 30.000},
    {"fecha": "2024-03-24", "producto": "Crema",
     "cantidad": 10, "precio": 250.000},
    {"fecha": "2024-03-10", "producto": "Harina",
     "cantidad": 3, "precio": 120.000},
    {"fecha": "2024-04-20", "producto": "Mantequilla",
     "cantidad": 3, "precio": 50.000},
    {"fecha": "2024-04-29", "producto": "EsenciaVainilla",
     "cantidad": 2, "precio": 12.000},
    {"fecha": "2024-05-23", "producto": "Mantequilla",
     "cantidad": 2, "precio": 12.000},
    {"fecha": "2024-05-08", "producto": "Azucar",
     "cantidad": 5, "precio": 50.000}]


def CargarD_Ventas(ventas):
    print(ventas)
    print("______________________________________________________________________________")


CargarD_Ventas(ventas)

# 2. Cálculo de Ingresos Totales
# Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas
# las ventas. Los ingresos totales se calculan multiplicando la cantidad vendida por el precio
# unitario para cada venta y sumando los resultados.


IngresosTotales = 0
for venta in ventas:
    print(f"Venta actual: {venta}")
    print(f"Cantidad: {venta['cantidad']}, Precio: {venta['precio']}")
    IngresosTotales += venta["cantidad"] * venta["precio"]
    print("___________________________")
print(f"Ingresos Totales: ${IngresosTotales:2f}")
print("_____________________________________________________________")

# Análisis del Producto Más Vendido:
# Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
# Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

Ventas_Producto_Mas_Vendido = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in Ventas_Producto_Mas_Vendido:
        Ventas_Producto_Mas_Vendido[producto] += cantidad
    else:
        Ventas_Producto_Mas_Vendido[producto] = cantidad

producto_mas_vendido = max(
    Ventas_Producto_Mas_Vendido, key=Ventas_Producto_Mas_Vendido.get)
print(
    f"\nProducto más vendido: {producto_mas_vendido} (Cantidad: {Ventas_Producto_Mas_Vendido[producto_mas_vendido]})")
print("_____________________________________________________________")

# Promedio de Precio por Producto:
# Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
# Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.


precios_por_producto = {}
print("\nCalculando el Promedio de Precio por Producto:")
for venta in ventas:
    producto = venta["producto"]
    precio_venta = venta["precio"]
    cantidad_vendida = venta["cantidad"]

    if producto in precios_por_producto:
        suma_precios, total_cantidad = precios_por_producto[producto]
        precios_por_producto[producto] = (
            suma_precios + (precio_venta * cantidad_vendida), total_cantidad + cantidad_vendida)
    else:
        precios_por_producto[producto] = (
            precio_venta * cantidad_vendida, cantidad_vendida)

print("\nDiccionario de Suma de Precios y Cantidad por Producto:")
for producto, (suma_precios, total_cantidad) in precios_por_producto.items():
    print(f"  {producto}: (Suma de Precios: ${suma_precios:.2f}, Cantidad Total: {total_cantidad})")

print("\nPrecio Promedio de Venta por Producto:")
for producto, (suma_precios, total_cantidad) in precios_por_producto.items():
    if total_cantidad > 0:
        precio_promedio = suma_precios / total_cantidad
        print(f"  {producto}: ${precio_promedio:.2f}")
    else:
        print(f"  {producto}: No se vendieron unidades.")
print("_____________________________________________________________")


# Ventas por Día:
# Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
# Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

Ingresos_Por_Dia = {}
print("\nCalculando Ingresos por Día:")
for venta in ventas:
    fecha = venta["fecha"]
    ingreso_venta = venta["cantidad"] * venta["precio"]
    if fecha in Ingresos_Por_Dia:
        Ingresos_Por_Dia[fecha] += ingreso_venta
    else:
        Ingresos_Por_Dia[fecha] = ingreso_venta

print("\nIngresos Total por Día:")
for fecha, ingresos in Ingresos_Por_Dia.items():
    print(f"  {fecha}: ${ingresos:.2f}")
print("_____________________________________________________________")


# Representación de Datos:
# Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
# «cantidad_total»: la cantidad total vendida del producto.
# «ingresos_totales»: los ingresos totales generados por la venta del producto.
# «precio_promedio»: el precio promedio de venta del producto.

Resumen_Ventas = {}
for producto in Ventas_Producto_Mas_Vendido:
    cantidad_total = Ventas_Producto_Mas_Vendido[producto]
    ingresos_totales_producto = 0
    total_cantidad_producto = 0
    for venta in ventas:
        if venta["producto"] == producto:
            ingresos_totales_producto += venta["cantidad"] * venta["precio"]
            total_cantidad_producto += venta["cantidad"]
    precio_promedio_producto = (
        ingresos_totales_producto / total_cantidad_producto
        if total_cantidad_producto > 0
        else 0
    )
    Resumen_Ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio_producto,

    }

print("\nResumen de Ventas por Producto:")
for producto, resumen in Resumen_Ventas.items():
    print(f"  {producto}:")
    print(f"    Cantidad Total: {resumen['cantidad_total']}")
    print(f"    Ingresos Totales: ${resumen['ingresos_totales']:.2f}")
    print(f"    Precio Promedio: ${resumen['precio_promedio']:.2f}")
print("_____________________________________________________________")
