class Ventana:
    __titulo = ''
    __xsi = 0
    __ysi = 0
    __xid = 0
    __yid = 0

    def __init__(self, t, xsi=0, ysi=0, xid=500, yid=500):
        self.__titulo = t
        self.__xsi = xsi
        self.__ysi = ysi
        self.__xid = xid
        self.__yid = yid

    def mostrar(self):
        print(
            'TITULO: {}\nX VERTICE SUPERIOR IZQ: {}\nY VERTICE SUPERIOR IZQ: {}\nX VERTICE INFERIOR DERECHO: {}\nY VERTICE INFERIOR DERECHO: {}'.format(
                self.__titulo, self.__xsi, self.__ysi, self.__xid, self.__yid))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return (self.__yid - self.__ysi)

    def ancho(self):
        return (self.__xid - self.__xsi)

    def moverDerecha(self, desp=1):
        self.__xid += desp
        self.__xsi += desp

    def moverIzquierda(self, desp=1):
        self.__xid -= desp
        self.__xsi -= desp

    def bajar(self, desp=1):
        self.__yid -= desp
        self.__ysi -= desp

    def subir(self, desp=1):
        self.__yid += desp
        self.__ysi += desp
