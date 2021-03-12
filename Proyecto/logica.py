from transformar_sistemas_numericos import *

# Convierte un numero binario a decimal, octal y hexadecimal.


def convertir_binario_h_o_d(binary_num):
    print("Numero ingresado: " + binary_num)
    if not is_binary(binary_num):
        print("El numero ingresado no es binario")
        return
    decimal = binary_to_decimal(binary_num)
    print("Equivalente en decimal: " + decimal)
    print("Equivalente en octal: " + decimal_to_octal(decimal))
    print("Equivalente en hexadecimal: " + decimal_to_hexadecimal(decimal))
    print()

