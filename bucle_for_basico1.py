# Básico: imprime todos los números enteros del 0 al 100.
for F in range(0, 101):
    print(F)

# Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for A in range(0, 500, 2):
    print(A)

# Contando Vanilla Ice: imprime los números enteros del 1 al 100.
# Si es divisible por 5 imprime “ice ice” en vez del número.
# Si es divisible por 10, imprime “baby”

for B in range(1, 101):

    if B % 10 == 0:
        print("BaBy")
    elif B % 5 == 0:
        print("Ice Ice")
    else:
        print(f"{B}")

# Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e
# imprime la suma total. (Sorpresa, será un número gigante).

suma_par = 0
for numero in range(0, 500001):
    if numero % 2 == 0:
        suma_par += numero
print("La suma de los números total es:", suma_par)

# Regrésame al 3: imprime los números positivos comenzando desde 2024,
# en cuenta regresiva de 3 en 3.
print("cuenta regresivo ==========================")
for B in range(2024, -1, -1):
    if B % 3 == 0:
        print(B)


# Contador dinámico: establece tres variables: numInicial, numFinal y multiplo.
# Comenzando en numInicial y pasando por numFinal, imprime los números enteros
# que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10,
# y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

numI = 3
numF = 10
multiplo = 2

for numero in range(numI, numF + 1):
    if numero % multiplo == 0:
        print(numero)
