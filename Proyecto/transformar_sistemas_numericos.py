# Esta libreria incluye las funciones necesarias para transformar sistemas numericos
# Nota: Todas las funciones de transformar sistemas devuelven el resultado como string
# al cual se le puede aplicar un cambio a futuro si asi se desea ya sea con int() o float()

# Funciones disponibles:

# Funciones auxiliar:
#
# is_binary(value): Devuelve 1 si value es binario, 0 de lo contrario
# equivalente_hexadecimal(num): Devuelve el equivalente en hexadecimal de un numero menor a 16
# divisiones_sucesivas(value, divisor): Devuelve el resultado de las divisiones sucesivas con el divisor
# multiplicaciones_sucesivas(value, multiplicaciones): Devuelve el resultado de las multiplicaciones sucesivas con
# el multiplicador

# Funciones principales:

# binary_to_decimal(value): Convierte value de binario a decimal y lo devuelve como string
# decimal_to_octal(value): Convierte value de decimal a octal y lo devuelve como string
# decimal_to_hexadecimal(value): Convierte value de decimal a hexadecimal y lo devuelve como string

##########################################################################################
##########################################################################################

# Retorna 1 si value es binario
# Retorna 0 si value no es binario

def is_binary(value):

    if value.count(".") > 1:
        return 0

    for x in value:
        if x != "0" and x != "1" and x != ".":
            return 0
    return 1

# Devuelve el equivalente en caracter de un numero decimal menor a 16


def equivalente_hexadecimal(num):
    if num == 15:
        return "F"
    elif num == 14:
        return "E"
    elif num == 13:
        return "D"
    elif num == 12:
        return "C"
    elif num == 11:
        return "B"
    elif num == 10:
        return "A"
    else:
        return str(num)

# Realiza el proceso de divisiones sucesivas a partir de un valor y el divisor


def divisiones_sucesivas(value, divisor):
    resultado = ""
    num = int(value)

    if num < 16 and divisor == 16:
        return equivalente_hexadecimal(num)

    while num >= divisor:
        if num%divisor < 10:
            resultado += str(num % divisor)
        elif num%divisor > 10 and divisor == 16:
            resultado += equivalente_hexadecimal(num%divisor)
        num = num//divisor
    resultado += str(num)
    return resultado[::-1]

# Realiza el proceso de multiplicaciones sucesivas a partir de un valor y el multiplicador


def multiplicaciones_sucesivas(value, multiplicador):
    num = float("0" + value)
    resultado = ""
    counter = 0

    while counter < 4:
        resto = num*multiplicador
        indice_coma = str(resto).index(".")
        resultado += str(int(resto))
        resto = float("0"+ str(resto)[indice_coma::])
        num = resto
        counter = counter + 1
    return resultado

###################################################################
# Convierte un numero de base 2 a base 10
###################################################################


def binary_to_decimal(value):

    if is_binary(value):
        if "." in value:
            return str(binary_to_decimal_coma_aux(value))
        return str(binary_to_decimal_aux(value))
    else:
        return "Ha ingresado un número no binario."


def binary_to_decimal_aux(value):
    n = len(value)-1
    result = 0
    for x in value:
        result += int(x) * (2**n)
        n = n - 1
    return result


def binary_to_decimal_coma_aux(value):
    n = value.index(".")-1
    result = 0
    for x in value:
        if x != ".":
            result += int(x) * (2**n)
            n = n - 1
    return result


###################################################################
# Convierte un numero de base 10 a base 8
###################################################################


def decimal_to_octal(value):
    if "." in value:
        return str(decimal_to_octal_coma_aux(value))
    return str(decimal_to_octal_aux(value))


def decimal_to_octal_aux(value):
    return divisiones_sucesivas(value, 8)


def decimal_to_octal_coma_aux(value):
    resultado = ""
    indice_coma = value.index(".")
    resultado += str(divisiones_sucesivas(value[:indice_coma], 8))
    resultado += "." + str(multiplicaciones_sucesivas(value[indice_coma::], 8))

    return resultado


###################################################################
# Convierte un numero de base 10 a base 16
###################################################################


def decimal_to_hexadecimal(value):
    if "." in value:
        return decimal_to_hexadecimal_coma_aux(value)
    return decimal_to_hexadecimal_aux(value)


def decimal_to_hexadecimal_aux(value):
    return divisiones_sucesivas(value, 16)


def decimal_to_hexadecimal_coma_aux(value):
    resultado = ""
    indice_coma = value.index(".")
    resultado += str(divisiones_sucesivas(value[:indice_coma], 16))
    resultado += "." + str(multiplicaciones_sucesivas(value[indice_coma::], 16))

    return resultado

