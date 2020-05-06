class Campo:
    def __init__(self):
        self.coordenadasde_borrachos = {}

    def add_borracho(self, borracho, coordenada):
        self.coordenadasde_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadasde_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadasde_borrachos[borracho] = nueva_coordenada

    def obtener_coodernada(self, borracho):
        return self.coordenadasde_borrachos[borracho]