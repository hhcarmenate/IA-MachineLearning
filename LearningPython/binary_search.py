objective = int(input('escoje un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objective)
response = (alto + bajo) / 2

while abs(response ** 2 - objective) >= epsilon:
    print(f'bajo = {bajo}, alto = {alto}, response = {response}')
    if response ** 2 < objective:
        bajo = response
    else:
        alto = response

    response = (alto + bajo) / 2

print(f'La raiz cuadrada de {objective} es {response}')