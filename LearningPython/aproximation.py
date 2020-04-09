objective = int(input('Escoge un numero: '))
epsilon = 0.01
paso = epsilon**2
response = 0.0

while abs(response ** 2 - objective) >= epsilon and response <= objective:
    print(abs(response ** 2 - objective),response)
    response += paso

if abs(response ** 2 - objective) >= epsilon:
    print(f'No se encontro la raizl cuadrada del {objective}')
else:
    print(f'La raiz cuadrada de {objective} es {response}')