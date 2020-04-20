def suma(a, b):
    """
    Suma los valores de a + b.

    :param a: any number
    :param b: any number
    :return: sum a and b
    """
    total = a + b
    return total

print(suma(1,5))

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

print(nombre_completo('Henry', 'Carmenate'))
print(nombre_completo('Henry', 'Carmenate', inverso=True))
print(nombre_completo(apellido='Carmenate', nombre='Henry'))