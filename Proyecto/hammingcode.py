from transformar_sistemas_numericos import *


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
    salta = n - 1
    while comprueba < tamano_final:
        comprueba = comprueba + salta
        for x in range(n):
            if comprueba <= tamano_final:
                resultado.append(comprueba)
            comprueba += 1
        salta = n
    return resultado


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


def obtener_lista_bits_datos(lista_pos_paridad, binary_num):
    resultado = []
    pos = 1
    i = 0
    while pos <= 17:
        if pos not in lista_pos_paridad:
            resultado.append((pos, binary_num[i]))
            i += 1
        pos += 1
    return resultado


def calcula_posiciones_bits_datos(lista_pos_paridad):
    resultado = []
    pos = 1
    i = 0
    while pos <= 17:
        if pos not in lista_pos_paridad:
            resultado.append(pos)
            i += 1
        pos += 1
    return resultado


def crea_matriz(filas, columnas):
    matrix = []
    for i in range(filas):
        matrix.append([])
        for j in range(columnas):
            matrix[i].append(" ")
    return matrix


def agregar_bits_paridad_a_matriz(matriz, lista_bits_paridad):
    i = 0
    for x in lista_bits_paridad:
        matriz[i][x - 1] = "x"
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
            if matriz[i][x - 1] != "x":
                if (x, '0') in lista_bits_datos:
                    matriz[i][x - 1] = "0"
                elif (x, '1') in lista_bits_datos:
                    matriz[i][x - 1] = "1"
        i += 1


def calcular_valor_paridades(matriz, paridad):
    if paridad == "par":

        for f in matriz:
            if is_par(f.count("1")) == 1:
                f[f.index("x")] = "0"
            else:
                f[f.index("x")] = "1"

    else:
        for f in matriz:
            if is_par(f.count("1")) == 1:
                f[f.index("x")] = "1"
            else:
                f[f.index("x")] = "0"


def obtener_matriz_sin_bits_paridad_verificados(binary_num):
    cantidad_bits_paridad = 5
    tamano_final = 17

    lista_bits_paridad = calcula_posiciones_bits_paridad(tamano_final)
    lista_bits_datos = obtener_lista_bits_datos(lista_bits_paridad, binary_num)

    matriz = crea_matriz(cantidad_bits_paridad, tamano_final)

    agregar_bits_paridad_a_matriz(matriz, lista_bits_paridad)
    agregar_bits_datos_a_matriz(matriz, lista_bits_paridad, lista_bits_datos, tamano_final)

    return matriz


def obtener_matriz_tabla_1(binary_num, paridad):
    if len(binary_num) != 12:
        print("el numero ingresado debe ser de 12 bits")
        return False

    matriz = obtener_matriz_sin_bits_paridad_verificados(binary_num)
    calcular_valor_paridades(matriz, paridad)
    return matriz


def obtener_numero_sin_bits_paridad(binary_num_with_hamming):
    resultado = ""
    bits_datos = calcula_posiciones_bits_datos(calcula_posiciones_bits_paridad(17))
    i = 1
    for x in binary_num_with_hamming:
        if i in bits_datos:
            resultado += x
        i += 1
    return resultado


def agregar_bits_paridad(binary_num_with_error, matriz, paridad):
    posiciones_bits_paridad = calcula_posiciones_bits_paridad(17)
    i = 0
    analisis_filas = []

    for x in posiciones_bits_paridad:

        if is_par(matriz[i].count("1")):
            if binary_num_with_error[x - 1] == "1":
                if paridad == "par":
                    analisis_filas.append("1")
                else:
                    analisis_filas.append("0")
            else:
                if paridad == "par":
                    analisis_filas.append("0")
                else:
                    analisis_filas.append("1")
        else:
            if binary_num_with_error[x - 1] == "0":
                if paridad == "par":
                    analisis_filas.append("1")
                else:
                    analisis_filas.append("0")

            else:
                if paridad == "par":
                    analisis_filas.append("0")
                else:
                    analisis_filas.append("1")

        matriz[i][x - 1] = binary_num_with_error[x - 1]
        i += 1

    if paridad == "par":

        return analisis_filas

    else:
        print("prueba prueba:")
        print(analisis_filas)
        print(analisis_filas[::-1])
        return reemplazar_1_por_0_array(analisis_filas)


def reemplazar_1_por_0_array(num):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("prueba: " + str(num))
    resultado = []
    i = 0

    for x in num:
        if x == "0":
            resultado.append("1")
        else:
            resultado.append("0")
        i += 1
    return resultado


def reemplazar_1_por_0(num):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
    print("prueba: " + str(num))
    resultado = ""
    i = 0

    for x in num:
        if x == "0":
            resultado += "1"
        else:
            resultado += "0"
        i += 1
    print("resultado: " + resultado)
    return resultado


def calcular_posicion_error(lista_analisis, paridad):

    print(paridad)

    if paridad == "par":
        print("XXXXXXXXXXXXXX")
        return binary_to_decimal("".join(lista_analisis))
    else:
        print("aAASDASDA")
        return binary_to_decimal(reemplazar_1_por_0("".join(lista_analisis)))


def verificar_errores_tabla_2(binary_num_with_error, paridad):
    if len(binary_num_with_error) != 17:
        print("el numero ingresado debe ser de 17 bits, 5:paridad, 12:datos")
        return 0

    num = obtener_numero_sin_bits_paridad(binary_num_with_error)

    matriz = obtener_matriz_sin_bits_paridad_verificados(num)

    resultado_analisis = agregar_bits_paridad(binary_num_with_error, matriz, paridad)

    print_matriz(matriz)
    print("PRUEBA RESULTADO ANALISIS")
    print(resultado_analisis)

    error = calcular_posicion_error(resultado_analisis[::-1], paridad)

    # print("El error se encuentra en el bit: " + str(error))

    return (matriz, error, resultado_analisis)





def palabra_con_paridad(matriz):
    resultado = []
    for i in range(len(matriz[0])):
        resultado.append("x")
    column = 0
    for f in matriz:
        for c in f:
            if c != " ":
                resultado[column] = c
            column += 1
        column = 0

    return "".join(resultado)


def print_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


num3 = "011011111110"

print("Tabla 1 resultante del numero de entrada: " + num3)


matriz = obtener_matriz_tabla_1(num3, "par")
print_matriz(matriz)
print("La palabra final con paridad es: " + str(palabra_con_paridad(matriz)))

num4 = "11001101111111100"

print("Verificando error en el numero:  " + num4)
result = verificar_errores_tabla_2(num4, "par")
print(result)
