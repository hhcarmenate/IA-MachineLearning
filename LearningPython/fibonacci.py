def fibonacci(n):
    """
    Calc fibonacci serie
    :param n: position
    :return: number in that position
    """
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Entre la posicion de la serie de fibonacci que desea conocer: '))
print(f'El valor de fibonacci en esa posicion es {fibonacci(n)}')
