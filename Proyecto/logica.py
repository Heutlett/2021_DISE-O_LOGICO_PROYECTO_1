from transformar_sistemas_numericos import *

# Convierte un numero binario a decimal, octal y hexadecimal.


def convertir_binario_h_o_d(binary_num):
    print("numero ingresado: " + binary_num)
    if not is_binary(binary_num):
        print("el numero ingresado no es binario")
        print()
        return
    decimal = binary_to_decimal(binary_num)
    print("equivalente en decimal: " + decimal)
    print("equivalente en octal: " + decimal_to_octal(decimal))
    print("equivalente en hexadecimal: " + decimal_to_hexadecimal(decimal))
    print()

"""

funcion obtener_codigo_nrzi
recibe: un numero binario en tipo string y un parametro de inicio

"""


def obtener_codigo_nrzi(binary_num, empieza_en):

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
