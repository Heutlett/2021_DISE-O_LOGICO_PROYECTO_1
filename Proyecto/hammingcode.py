def is_par(num):
    if num == 0:
        return 1
    elif num % 2 == 0:
        return 1
    else:
        return 0

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

"""
Calcula las posiciones donde se deben poner numeros para cada fila de bit de paridad, por ejemplo:
[(3, '0'), (5, '1'), (6, '1'), (7, '0'), (9, '1'), (10, '0'), (11, '1')]
En la posicion 3 debe ir un 0
En la posicion 5 debe ir un 1
etc...
"""

def calcula_posiciones_bits_datos(lista_pos_paridad, tamano_final, binary_num):
    resultado = []
    pos = 1
    i = 0
    while pos <= tamano_final:
        if pos not in lista_pos_paridad:
            resultado.append((pos, binary_num[i]))
            i += 1
        pos += 1
    return resultado


def crea_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append("-")
    return matriz

def agregar_bits_paridad_a_matriz(matriz, lista_bits_paridad):
    i = 0
    for x in lista_bits_paridad:
        matriz[i][x-1] = "x"
        i += 1
    return matriz

"""
Recorre la lista de bits de paridad, obteniendo de ella la posicion de cada bit de paridad
para posteriormente llamar a la funcion regla_salga_comprueba la cual devolverá una lista
con las posiciones de los valores que debe analizar, es decir para un bit de paridad en la 
posicion 1 se tendria que debe comprobar los siguientes valores:
[1, 3, 5, 7, 9, 11]    <--- Valores que analiza el bit de paridad en la posicion 1

[2, 3, 6, 7, 10, 11]   <--- Valores que analiza el bit de paridad en la posicion 2
[4, 5, 6, 7]           <--- Valores que analiza el bit de paridad en la posicion 4
[8, 9, 10, 11]         <--- Valores que analiza el bit de paridad en la posicion 8

Finalmente consulta que valor debe ir en cada bit de dato con la lista que devuelve la funcion
calcula_posiciones_bits_datos que devuelve algo como esto:
[(3, '0'), (5, '1'), (6, '1'), (7, '0'), (9, '1'), (10, '0'), (11, '1')]
"""


def agregar_bits_datos_a_matriz(matriz, lista_bits_paridad, lista_bits_datos, tamano_final):
    i = 0
    for p in lista_bits_paridad:
        lista_posicion = regla_salta_comprueba(p, tamano_final)
        for x in lista_posicion:
            if matriz[i][x-1] != "x":
                if (x, '0') in lista_bits_datos:
                    matriz[i][x-1] = "0"
                elif (x, '1') in lista_bits_datos:
                    matriz[i][x - 1] = "1"
        i += 1



def calcular_valor_paridades(matriz):

    for f in matriz:
        if is_par(f.count("1")) == 1:
            f[f.index("x")] = "0"
        else:
            f[f.index("x")] = "1"



def llenar_matriz(binary_num):

    cantidad_bits_paridad = calcula_cantidad_bits_paridad(binary_num)
    tamano_final = cantidad_bits_paridad + len(binary_num)

    lista_bits_paridad = calcula_posiciones_bits_paridad(tamano_final)
    lista_bits_datos = calcula_posiciones_bits_datos(lista_bits_paridad, tamano_final, binary_num)

    matriz = crea_matriz(cantidad_bits_paridad, tamano_final)

    agregar_bits_paridad_a_matriz(matriz, lista_bits_paridad)
    agregar_bits_datos_a_matriz(matriz, lista_bits_paridad, lista_bits_datos, tamano_final)

    calcular_valor_paridades(matriz)
    return matriz


def palabra_con_paridad(matriz):
    resultado = []
    for i in range(len(matriz[0])):
        resultado.append("x")
    column = 0
    for f in matriz:
        for c in f:
            if c != "-":
                resultado[column] = c
            column += 1
        column = 0

    return resultado


def orden_de_titulo_columnas(lista_bits_paridad, tamano_final):
    resultado = []
    for i in range(tamano_final):
        resultado.append("")
    p = 1
    for i in lista_bits_paridad:
        resultado[i-1] = "p" + str(p)
        p += 1
    d = 1
    for i in range(tamano_final):
        if resultado[i] == "":
            resultado[i] = "d" + str(d)
            d += 1

    return resultado


def print_matriz(matriz):

    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

print("Regla donde colocar bits datos para bit de paridad en pos 1 " + str(regla_salta_comprueba(1, 11)))
print("Regla donde colocar bits datos para bit de paridad en pos 2 " + str(regla_salta_comprueba(2, 11)))
print("Regla donde colocar bits datos para bit de paridad en pos 4 " + str(regla_salta_comprueba(4, 11)))
print("Regla donde colocar bits datos para bit de paridad en pos 8 " + str(regla_salta_comprueba(8, 11)))


num = "0110101"
num2 = "0110101"
num3 = "0110101"

listax = calcula_posiciones_bits_paridad(11)

print("la cantidad de bits de paridad para " + num + " es " + str(calcula_cantidad_bits_paridad(num)))
print("la cantidad de bits de paridad para " + num + " es " + str(calcula_cantidad_bits_paridad(num2)))
print("los bits de paridad para " + num3 + " deben estar en las posiciones " + str(listax))
print("los bits de datos para " + num3 + " deben estar en las posiciones " + str(calcula_posiciones_bits_datos(listax, 11, num)))

print("Primera fila de la tabla que tiene el orden")
print(orden_de_titulo_columnas(listax, 11))
matriz = llenar_matriz(num3)
print_matriz(matriz)
print("La palabra final con paridad es :" + str(palabra_con_paridad(matriz)))

