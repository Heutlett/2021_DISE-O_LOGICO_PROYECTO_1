"""
Cada bit de paridad se obtiene calculando la paridad de alguno de los bits de datos. La posición del bit de paridad
determina la secuencia de los bits que alternativamente comprueba y salta, a partir de éste, tal y como se explica a
continuación.
Regla general para la posición n es: salta n-1 bits, comprueba n bits, salta n bits, comprueba n bits...
Posición 1: salta 0, comprueba 1, salta 1, comprueba 1, etc. Posición 2: salta 1, comprueba 2, salta 2, comprueba 2, etc
Posición 4: salta 3, comprueba 4, salta 4, comprueba 4, etc.
En la Posición 1 (2^0 = 1), comprobaríamos los bits: 1, 3, 5, 7, 9, 11, 13...
En la Posición 2 (2^1 = 2), los bits: 2, 3, 6, 7, 10, 11, 14, 15...
En la Posición 4 (2^2 = 4), los bits: 4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23...
"""


def regla_salta_comprueba(n, tamano_final):
    resultado = []
    comprueba = 1
    salta = n-1
    while comprueba < tamano_final:
        comprueba = comprueba + salta
        for x in range(n):
            if comprueba <= tamano_final:
                resultado.append(comprueba)
            comprueba += 1
        salta = n
    return resultado

"""
Calcula la cantidad de bits de paridad de un numero binario, siguiendo la regla de que por cada 4 bits de datos
se agregan 3 bits de paridad y finalmente se le suma el bits de paridad general
"""


def calcula_cantidad_bits_paridad(binary_num):
    return (len(binary_num)//4)*3+1

"""
1. Todos los bits cuya posición es potencia de dos se utilizan como bits de 
paridad (posiciones 1, 2, 4, 8, 16, 32, 64, etc.). 
"""


def calcula_posiciones_bits_paridad(tamano_final):
    resultado = []
    i = 0
    num = 2 ** i
    while num < tamano_final:
        resultado.append(num)
        i += 1
        num = 2 ** i
    return resultado


def calcula_posiciones_bits_datos(lista_pos_paridad, tamano_final):
    resultado = []
    pos = 1
    while pos <= tamano_final:
        if pos not in lista_pos_paridad:
            resultado.append(pos)
        pos += 1
    return resultado


def crea_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(None)
    return matriz


def llenar_matriz(binary_num):
    cantidad_bits_paridad = calcula_cantidad_bits_paridad(binary_num)
    tamano_final = cantidad_bits_paridad + len(binary_num)
    lista_bits_paridad = calcula_posiciones_bits_paridad(tamano_final)
    lista_bits_datos = calcula_posiciones_bits_datos(lista_bits_paridad, tamano_final)
    matriz = crea_matriz(cantidad_bits_paridad, tamano_final)
    i = 0
    for x in lista_bits_paridad:
        matriz[i][x-1] = "x"
        i += 1
    


    print_matriz(matriz)


def print_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

print(regla_salta_comprueba(1, 11))
print(regla_salta_comprueba(2, 11))
print(regla_salta_comprueba(4, 11))
print(regla_salta_comprueba(8, 11))
num = "1010101"
num2 = "101010101010"
num3 = "0110101"
listax = calcula_posiciones_bits_paridad(11)
print("la cantidad de bits de paridad para " + num + " es " + str(calcula_cantidad_bits_paridad(num)))
print("la cantidad de bits de paridad para " + num + " es " + str(calcula_cantidad_bits_paridad(num2)))
print("los bits de paridad para " + num3 + " deben estar en las posiciones " + str(listax))
print("los bits de datos para " + num3 + " deben estar en las posiciones " + str(calcula_posiciones_bits_datos(listax, 11)))
llenar_matriz(num3)