from borracho import BorrachoTRadicional
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coodernada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coodernada(borracho))

def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(name='david')
    origen = Coordenada(0, 0)
    distance = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.add_borracho(borracho,origen)
        simular_caminata = caminata(campo, borracho, pasos)
        distance.append(round(simular_caminata,1))

    return distance

def graficar(x,y):
    grafica = figure(title='Camino de borracho', x_axis_label = 'pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)


def main(distancias_de_caminata, intentos, tipo_borracho):
    distancias_media_por_caminata = []

    for pasos  in  distancias_de_caminata:
        distancias = simular_caminata(pasos, intentos,tipo_borracho)
        distancia_media = round(sum(distancias)/ len(distancias_de_caminata),4)
        distancia_maxima = max(distancias)
        distancia_min = min(distancias)
        distancias_media_por_caminata.append(distancia_media)

        print(f'{tipo_borracho.__name__} caminata aleatorea de {pasos} pasos')
        print(f'media = {distancia_media}')
        print(f'max = {distancia_maxima}')
        print(f'min = {distancia_min}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTRadicional)