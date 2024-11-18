import math as m
import numpy as np


def suma(*numeros) -> int:
    """Esta funcion suma

    Args:
        a (int): Operando 1
        b (int): Operando 2

    Returns:
        int: La suma
    """
    sum = 0
    for i in numeros:
        sum += i
    return sum

print(suma(1,2,3,4,5,6,7,8,9))