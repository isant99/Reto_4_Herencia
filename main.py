from operator import attrgetter

#interfaz "Entregable"
class Entregable:
    def entregar(self):
        pass
    def devolver(self):
        pass
    def isEntregado(self):
        pass
    def compareTo(self, object):
        pass

class Serie(Entregable):
    #Propiedades
    __titulo = ''
    __temporadas = 3
    __genero =''
    __creador =''
    entregado = False

    def __init__(self, titulo, genero, creador):
        self.__titulo = titulo
        self.__genero = genero
        self.__creador = creador

    #Gets y sets

    @property
    def titulo(self):
        return self.__titulo

    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def genero(self):
        return self.__genero

    @property
    def creador(self):
        return self.__creador

    @titulo.setter
    def titulo(self, nombretit):
        self.__titulo = nombretit

    @temporadas.setter
    def temporadas(self, numtemp):
        if numtemp <= 0:
            raise ValueError('Valor no permitido')
        self.__temporadas = numtemp

    @genero.setter
    def genero(self, nombregen):
        self.__genero = nombregen

    @creador.setter
    def creador(self, nombrecre):
        self.__creador = nombrecre

    #Metodos
    def __str__(self):
        return f'Titulo: {self.titulo}, Temporadas: {self.temporadas}, Genero: {self.genero}, Creador: {self.creador}'

    def entregar(self):
        if self.entregado == False:
            self.entregado = True
        else:
            print(f'{self.titulo} ya esta entregado')

    def devolver(self):
        if self.entregado == True:
            self.entregado = False
        else:
            print(f'{self.titulo} ya esta devuelto')

    def isEntregado(self):
        if self.entregado == True:
            print(f'{self.titulo} esta entregado')
            return True
        else:
            print(f'{self.titulo} no esta entregado')
            return False

    def compareTo(self, object):
        if self.temporadas > object.temporadas:
            return self
        elif self.temporadas < object.temporadas:
            return object
        else:
            return None

class Videojuego(Entregable):
    #Propiedades
    __titulo = ''
    __horas_estimadas = 10
    __genero = ''
    __compania = ''
    entregado = False

    def __init__(self, titulo, genero, compania):
        self.__titulo = titulo
        self.__genero  = genero
        self.__compania = compania

    #Gets y sets
    @property
    def titulo(self):
        return self.__titulo

    @property
    def horas_estimadas(self):
        return self.__horas_estimadas

    @property
    def genero(self):
        return self.__genero

    @property
    def compania(self):
        return self.__compania

    @titulo.setter
    def titulo(self,nombretit):
        self.__titulo = nombretit

    @horas_estimadas.setter
    def horas_estimadas(self, numhoras):
        if numhoras <= 0:
            raise ValueError('Valor no permitido')
        self.__horas_estimadas = numhoras

    @genero.setter
    def genero(self, nombregen):
        self.__genero = nombregen

    @compania.setter
    def compania(self,nombrecom):
        self.__compania = nombrecom

    #Metodos
    def __str__(self):
        return f'Titulo: {self.titulo}, Horas Estimadas: {self.horas_estimadas}, Genero: {self.genero}, Compañia: {self.compania}'

    def entregar(self):
        if self.entregado == False:
            self.entregado = True
        else:
            print(f'{self.titulo} ya esta entregado')

    def devolver(self):
        if self.entregado == True:
            self.entregado = False
        else:
            print(f'{self.titulo} ya esta devuelto')

    def isEntregado(self):
        if self.entregado == True:
            print(f'{self.titulo} esta entregado')
            return True
        else:
            print(f'{self.titulo} no esta entregado')
            return False

    def compareTo(self, object):
        if self.horas_estimadas > object.horas_estimadas:
            return self
        elif self.horas_estimadas < object.horas_estimadas:
            return object
        else:
            return None

if __name__ == '__main__':
    firegame = Videojuego('La llama', 'Accion', 'HotGames')
    watergame = Videojuego('Agua', 'Magia', 'CoolGames')
    watergame.horas_estimadas = 20
    watergame2 = Videojuego('Agua: el retorno', 'Magia', 'CoolGames')
    watergame.horas_estimadas = 25
    earthgame = Videojuego('Tierra de tierras', 'RPG', 'ToughGames')
    windgame = Videojuego('Vendaval', 'Indie', 'SoftGames')
    windgame.horas_estimadas = 5

    juegos = [firegame, watergame, watergame2, earthgame, windgame]

    serie1 = Serie('Perro magico', 'Infantil', 'Paco Sanchez')
    serie1.temporadas = 10
    serie2 = Serie('El de en medio de los Chichos', 'Comedia', 'Sara Benito')
    serie3 = Serie('Booo', 'Terror', 'Lidia Serrano')
    serie4 = Serie('La migracion de los escarabajos', 'Documental', 'Pedro Piqueras')
    serie4.temporadas = 1
    serie5 = Serie('Suavementeeee, besame', 'Romance', 'Lara Croft')
    serie5.temporadas = 7

    series = [serie1, serie2, serie3, serie4, serie5]

    for i in range(len(series)):
        if i%2 == 0:
            series[i].entregar()
            juegos[i].entregar()

    series_entregadas = 0
    for serie in series:
        if serie.isEntregado() == True:
            series_entregadas += 1
            serie.devolver()

    print(f'Habia {series_entregadas} series entregadas')

    juegos_entregados = 0
    for juego in juegos:
        if juego.isEntregado() == True:
            juegos_entregados += 1
            juego.devolver()

    print(f'Habia {juegos_entregados} juegos entregados')

    seriemax = max(series, key=attrgetter('temporadas'))
    print('La serie con mas temporadas es:')
    print(seriemax)

    juegomax = max(juegos, key=attrgetter('horas_estimadas'))
    print('El juego con mas horas estimadas es:')
    print(juegomax)

