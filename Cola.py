import simpy



def sumOfDigits(numero):
    """Funcion para sumar todos los digitos del numero ingresado
        Esta funcion usa modulo 10 para poder encontrar cada digito"""
    resultado = 0
    while numero != 0:
        resultado = int(resultado + (numero % 10))
        numero = int(numero / 10)
    return resultado


print(sumOfDigits(123456789))
