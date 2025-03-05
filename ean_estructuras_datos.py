#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Universidad EAN (Bogotá - Colombia)
# Departamento de Sistemas
# Faculta de Ingeniería
#
# Proyecto EAN Python Collections
# @author Luis Cobo (lacobo@universidadean.edu.co)
# Fecha: Feb 11, 2025
# Versión: 0.0.1 -> 11 de febrero de 2025
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Definición de los tipos genéricos que usaremos
from typing import TypeVar, Generic, List

T = TypeVar('T')


# --------------------------------------------------------------------
class Lista(Generic[T]):
    """
    Clase Lista que permite manipular y gestionar un grupo de objetos.
    Una lista es una secuencia de cero o más elementos de un mismo tipo.
    """

    # Constructor
    def __init__(self):
        """
        Constructor de la clase. Crea una lista vacía
        """
        self.__datos = []


    # Propiedad que define el tamaño de la lista
    @property
    def tam(self) -> int:
        return len(self.__datos)


    def agregar(self, elem: T) -> None:
        """
        Agrega un elemento al final de la lista.
        :param elem: El elemento que vamos a agregar
        :return: None
        """
        self.__datos.append(elem)


    def insertar(self, elem: T, indice: int) -> None:
        """
        Agrega un elemento en la posición o índice especificado
        :param elem: el elemento que vamos a agregar
        :param indice: la posición o índice del elemento que vamos a agregar
        :return: None
        """
        self.__datos.insert(indice, elem)


    def insertar_al_principio(self, elem: T) -> None:
        """
        Añade un elemento como primero de la lista
        :param elem: el elemento que vamos a agregar
        :return: None
        """
        self.__datos.insert(0, elem)


    def eliminar(self, indice: int) -> None:
        """
        Elimina un elemento en la lista.
        :param indice: La posición o índice del elemento que vamos a eliminar
        :return: None
        """
        tamx = len(self.__datos)
        if -tamx <= indice < tamx:
            self.__datos.pop(indice)


    def __getitem__(self, indice: int) -> T:
        """
        Permite obtener el elemento que se encuentra en el indice dado
        :param indice: la posición en la lista
        :return: el elemento en el indice indicado
        """
        tamx = len(self.__datos)
        if -tamx <= indice < tamx:
            return self.__datos[indice]
        else:
            return None


    def __setitem__(self, indice: int, elem: T) -> None:
        """
        Permite cambiar el elemento que se encuentra en el indice dado
        :param indice: el índice del elemento a cambiar
        :param elem: el elemento que vamos a guardar en la lista
        :return: None
        """
        tamx = len(self.__datos)
        if -tamx <= indice < tamx:
            self.__datos[indice] = elem


    @property
    def indices(self):
        """
        Permite trabajar con el rango de los índices de la lista
        :return: un objeto rango
        """
        return range(self.tam)


    def __str__(self) -> str:
        """
        Permite obtener una representación como String de la lista
        :return: la lista guardada como un string
        """
        resultado = 'Lista['
        n = 1
        for elemento in self.__datos:
            resultado += str(elemento)
            if n < len(self.__datos):
                resultado += ', '
            n += 1
        resultado += ']'
        return resultado


    def contiene_elemento(self, elemento: T) -> bool:
        """
        Permite saber si el elemento hace parte de la lista
        :param elemento: el elemento a buscar
        :return: True si el elemento está en la lista. False si no
        """
        return elemento in self.__datos


    def indice_elemento(self, elemento: T) -> int | None:
        """
        Retorna la posición del elemento en la lista
        :param elemento: el elemento a buscar
        :return: El índice en que se encuentra el elemento en la lista
        basado en el índice cero. Retorna None si no se encuentra el elemento
        """
        for i in self.indices:
            elem = self[i]
            if elemento == elem:
                return i
        return None


    @property
    def vacia(self) -> bool:
        """
        Permite saber si la lista está vacía o no
        :return: True si la lista no tiene elementos y False si hay algún elemento
        """
        return len(self.__datos) == 0


    @property
    def primero(self) -> T:
        """
        Obtiene el primero de la lista
        :return: el primero de la lista
        """
        if len(self.__datos) > 0:
            return self.__datos[0]
        else:
            return None


    @property
    def ultimo(self) -> T:
        """
        Obtiene el ultimo de la lista
        :return: el ultimo de la lista
        """
        if len(self.__datos) > 0:
            return self.__datos[-1]
        else:
            return None


    def limpiar(self) -> None:
        """
        Elimina todos los elementos de la lista, dejándola vacía
        :return: None
        """
        self.__datos.clear()


    def __eq__(self, otra_lista) -> bool:
        """
        Permite saber si dos listas son iguales
        :param otra_lista:  la lista con la que nos comparamos
        :return: True si son iguales, False si no
        """
        if isinstance(otra_lista, Lista):
            return self.__datos == otra_lista.__datos
        else:
            return False


# ---------------------------------------------------------------------

def concatenar_listas(lista1: Lista[T], lista2: Lista[T]) -> Lista[T]:
    """
    Une dos listas, anexando los elementos de la lista2 al final de la lista1
    :param lista1: La lista a la izquierda
    :param lista2: La lista a la derecha
    :return: una lista con los elementos de la lista1 y la lista2
    """
    resultado = Lista[T]()
    for i in lista1.indices:
        elemento = lista1[i]
        resultado.agregar(elemento)

    for i in lista2.indices:
        elemento = lista2[i]
        resultado.agregar(elemento)

    return resultado


def crear_lista(*elementos: T) -> Lista[T]:
    """
    Permite crear una lista con los elementos recibidos como parámetro
    :param elementos: los datos a guardar en la lista
    :return: La nueva lista con los elementos recibidos
    """
    resultado = Lista[T]()
    for elemento in elementos:
        resultado.agregar(elemento)
    return resultado


def resto_lista(lista_original: Lista[T]) -> Lista[T]:
    """
    Retorna una nueva lista equivalente a la lista que se recibe como
    parámetro, pero sin el primer elemento. Usado en recursiones.
    :param lista_original: la lista con la que trabajamos
    :return: la misma lista, pero sin el primer elemento
    """
    resultado = Lista[T]()
    for indice in lista_original.indices:
        if indice >= 1:
            resultado.agregar(lista_original[indice])
    return resultado


def copiar_lista(lista: Lista[T]) -> Lista[T]:
    """
    Obtiene una copia idéntica de la lista que se recibe como
    parámetro.
    :param lista: la lista con la que trabajamos
    :return: una copia de la lista
    """
    resultado = Lista[T]()
    for indice in lista.indices:
        elemento = lista[indice]
        resultado.agregar(elemento)
    return resultado


# ---------------------------------------------------------------------
import pandas as pd
from dataclasses import dataclass

@dataclass
class Persona:
    """
    Clase que representa una persona
    """
    __cedula: int
    __nombre: str
    __edad: int
    __genero: str
    __num_hijos: int
    __nivel_educativo: str
    __estrato: int
    __ingresos: int
    __peso: int
    __altura: int
    __fuma: bool
    __usa_lentes: bool
    __tiene_casa: bool
    __tiene_automovil: bool

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def cedula(self) -> int:
        return self.__cedula

    @property
    def edad(self) -> int:
        return self.__edad

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def num_hijos(self) -> int:
        return self.__num_hijos

    @property
    def nivel_educativo(self) -> str:
        return self.__nivel_educativo

    @property
    def estrato(self) -> int:
        return self.__estrato

    @property
    def ingresos(self) -> int:
        return self.__ingresos

    @property
    def peso(self) -> int:
        return self.__peso

    @property
    def altura(self) -> int:
        return self.__altura

    @property
    def fuma(self) -> bool:
        return self.__fuma

    @property
    def usa_lentes(self) -> bool:
        return self.__usa_lentes

    @property
    def tiene_casa(self) -> bool:
        return self.__tiene_casa

    @property
    def tiene_automovil(self) -> bool:
        return self.__tiene_automovil


# ---------------------------------------------
def leer_archivo_personas() -> Lista[Persona]:
    """
    Permite crear una lista con las personas que están
    en el archivo
    :return: la lista con las personas
    """
    archivo = "https://github.com/luiscobo/poo/raw/refs/heads/main/people.csv"
    df = pd.read_csv(archivo, sep=";", encoding="utf-8")
    resultado = Lista[Persona]()
    for index, row in df.iterrows():
        cedula = row["Cedula"]
        nombre = row["Nombres"]
        edad = row["Edad"]
        genero = row["Genero"]
        num_hijos = row["No de hijos"]
        nivel_educativo = row["Nivel Educativo"]
        estrato = row["Estrato Socio"]
        ingresos = row["Ingresos"]
        peso = row["Peso"]
        altura = row["Talla"]
        fuma = row["Fuma"] == "SI"
        usa_lentes = row["Usa Lentes"] == "SI"
        tiene_casa = row["Tiene Casa"] == "SI"
        tiene_automovil = row["Tiene Automovil"] == "SI"
        p = Persona(cedula, nombre, edad, genero, num_hijos, nivel_educativo, estrato, ingresos, peso, altura, fuma, usa_lentes, tiene_casa, tiene_automovil)
        resultado.agregar(p)
    return resultado

  
# ---------------------------------------------------------------------
@dataclass(frozen=True)
class Departamento:
    """
    Clase que representa la información de un departamento de Colombia
    """
    nombre: str
    cant_municipios: int
    capital: str
    superficie: float
    poblacion: int
    densidad: float
    indice_desarrollo_humano: float
    fecha_creacion: int
    region: str


# ---------------------------------------------------------------------

def leer_archivo_departamentos() -> Lista[Departamento]:
    """
    Permite obtener una lista de departamentos a partir del archivo
    de datos que se encuentra en github
    :return: Una lista con la información de los departamentos
    """
    archivo = "https://raw.githubusercontent.com/luiscobo/poo/refs/heads/main/departamentos2.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    resultado = Lista[Departamento]()
    for index, row in df.iterrows():
        nombre = row["Departamento"]
        municipios = row["Municipios"]
        capital = row["Capital"]
        superficie = row["Superficie"]
        poblacion = row["Población"]
        densidad = row["Densidad"]
        idh = row["IDH6"]
        fecha = row["Fecha de creación"]
        region = row["Región"]
        depto = Departamento(nombre, cant_municipios=municipios, capital=capital, superficie=superficie,
                             poblacion=poblacion, densidad=densidad, indice_desarrollo_humano=idh, fecha_creacion=fecha,
                             region=region)
        resultado.agregar(depto)
    return resultado


# ---------------------------------------------------------------------
if __name__ == '__main__':
    lst = leer_archivo_departamentos()
    print(lst[0])
