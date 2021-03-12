from logica import *

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    num1 = "10101.01"
    num2 = "10102011"
    num3 = "11111111"
    num4 = "101.1010"
    num5 = "760"
    num6 = "760.33"
    num7 = "15"
    num8 = "124124"

    print(num1 + " B2 a decimal " + binary_to_decimal(num1))
    print(num2 + " B2 a decimal " + binary_to_decimal(num2))
    print(num3 + " B2 a decimal " + binary_to_decimal(num3))
    print(num4 + " B2 a decimal " + binary_to_decimal(num4))
    print(num5 + " B10 a octal " + decimal_to_octal(num5))
    print(num6 + " B10 a octal " + decimal_to_octal(num6))
    print(num7 + " B10 a hexadecimal " + decimal_to_hexadecimal(num7))
    print(num8 + " B10 a hexadecimal " + decimal_to_hexadecimal(num8))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
