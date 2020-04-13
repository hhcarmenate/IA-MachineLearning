def factorial(n):
    """
    Calc factorial number
    :param n: any integer bigger than 0
    :return: n factorial
    """
    if n == 1:
        return 1

    return n * factorial(n-1)

n = int(input('Enter a number: '))
print(factorial(n))