# Actualiza los valores en diccionarios y listas
# Cambia el valor de 3 en matriz por 6. Una vez realizado el
# cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]

matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6
print(matriz)

print("_____________________________")


# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes[0]["nombre"])
print("_____________________________")


# En ciudades, cambia “Cancún” por “Monterrey”

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)

print("__________________________________________________________")

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}]
coordenadas[0]["latitud"] = 9.9355431

print(coordenadas)

print("_______________________")


# 2. Iterar a través de una lista de diccionarios

def IterarDiccionario(lista):
    for diccionario in lista:
        output = ""
        for llave, valor in diccionario.items():
            output += f"{llave}: {valor}, "
        print(output[:-2])


print("2. Iterar a través de una lista de diccionarios:")
cantantes_ejemplo = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
IterarDiccionario(cantantes_ejemplo)


print("_______________________")


def IterarDiccionarioBonus(lista):
    for diccionario in lista:
        output = ""
        for llave, valor in diccionario.items():
            output += f"{llave} - {valor}, "
        print(output[:-2])


IterarDiccionarioBonus(cantantes_ejemplo)
print("_______________________")


# 3. Obtener valores de una lista de diccionarios


def iterarDiccionario2(llave, lista):
    print(f"3. Obtener valores para la llave '{llave}':")
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])


print("\nResultado iterarDiccionario2('nombre', cantantes_ejemplo):")
iterarDiccionario2("nombre", cantantes_ejemplo)

print("\nResultado iterarDiccionario2('pais', cantantes_ejemplo):")
iterarDiccionario2("pais", cantantes_ejemplo)


print("_______________________")

# 4. Iterar a través de un diccionario con valores de lista


def imprimirInformacion(diccionario):
    for llave, lista_valores in diccionario.items():
        tamaño = len(lista_valores)
        print(f"{tamaño} {llave.upper()}")
        for valor in lista_valores:
            print(valor)
        print(" ")


costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]}
imprimirInformacion(costa_rica)

print("_______________________")
