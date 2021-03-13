from transformar_sistemas_numericos import *

# Convierte un numero binario a decimal, octal y hexadecimal.


def convertir_binario_h_o_d(binary_num):
    if len(binary_num) == 0:
        return "Error, debe ingresar un número."
    resultado = ""
    resultado += "▸Numero ingresado: " + binary_num + "\n"
    if not is_binary(binary_num):
        return "El numero ingresado no es binario."

    decimal = binary_to_decimal(binary_num)
    resultado += "▸Equivalente en decimal: " + decimal + "\n"
    resultado += "▸Equivalente en octal: " + decimal_to_octal(decimal) + "\n"
    resultado += "▸Equivalente en hexadecimal: " + decimal_to_hexadecimal(decimal)
    return resultado
"""

funcion obtener_codigo_nrzi
recibe: un numero binario en tipo string y un parametro de inicio

"""


def obtener_codigo_nrzi(binary_num, empieza_en):

    if is_binary(binary_num) == 0:
        return "Error: El número ingresado no es binario."

    resultado = []
    resultado.append(empieza_en)
    estado = empieza_en
    anterior = binary_num[0]

    binary_num = binary_num[1:]
    for x in binary_num:
        if anterior == x:
            resultado.append(estado)
        elif anterior != x and estado == "bajo":
            estado = "alto"
            resultado.append(estado)
        elif anterior != x and estado == "alto":
            estado = "bajo"
            resultado.append(estado)
    return resultado
