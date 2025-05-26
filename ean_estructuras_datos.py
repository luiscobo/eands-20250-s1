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
import math
from math import sqrt
# Definición de los tipos genéricos que usaremos
from typing import TypeVar, Generic, List, Optional, Any
from collections.abc import Callable
from datetime import datetime


T = TypeVar('T')
R = TypeVar('R')


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


    def con_cada_elemento_haga(self, accion: Callable[..., None]) -> 'Lista[T]':
        """
        Realiza la misma operación sobre cada elemento de la lista,
        no modifica la lista original y la retorna
        :param accion: la operación a realizar sobre cada elemento de la lista
        :return: la lista original
        """
        for elemento in self.__datos:
            accion(elemento)
        return self


    def filtrar(self, predicado: Callable[..., bool]) -> 'Lista[T]':
        """
        Obtiene una lista con los elementos de la lista que cumplen con el predicado
        :param predicado: una función que devuelve True si el elemento cumple con el predicado
        :return: la lista de los elementos que cumplen con el predicado
        """
        resultado = Lista[T]()
        for elemento in self.__datos:
            if predicado(elemento):
                resultado.agregar(elemento)
        return resultado


    def seleccionar(self, selector: Callable[..., R]) -> 'Lista[R]':
        """
        Por cada elemento de la lista, aplica el selector y lo agrega a la lista de resultados
        :param selector: la operación a realizar sobre cada elemento de la lista
        :return: la lista conteniendo la aplicación del selector a cada elemento de la lista
        """
        resultado = Lista[R]()
        for elemento in self.__datos:
            resultado.agregar(selector(elemento))
        return resultado


    def transformar(self, selector: Callable[..., R]) -> 'Lista[R]':
        """
        Por cada elemento de la lista, aplica el selector y lo agrega a la lista de resultados
        :param selector: la operación a realizar sobre cada elemento de la lista
        :return: la lista conteniendo la aplicación del selector a cada elemento de la lista
        """
        resultado = Lista[R]()
        for elemento in self.__datos:
            resultado.agregar(selector(elemento))
        return resultado


    def acumular(self, valor_inicial: R, operacion: Callable[..., R]) -> R:
        """
        Acumula los diversos valores de la lista, arrancando en el valor
        inicial y aplicando la operación de izquierda a derecha a cada
        elemento de la lista
        :param valor_inicial: el valor inicial del acumulador
        :param operacion: la operación de acumulación a realizar sobre los elementos de la lista
        :return: el último valor del acumulador
        """
        acumulador = valor_inicial
        for elemento in self.__datos:
            acumulador = operacion(acumulador, elemento)
        return acumulador


    def reducir(self, operacion: Callable[..., T]) -> T:
        return self.acumular(self.primero, operacion)


    def sumar(self, selector: Callable[..., int | float] = None) -> int | float:
        """
        Halla la suma de todos los elementos de la lista
        :return: la suma de los elementos de la lista
        """
        if len(self.__datos) == 0:
            return 0.0
        if selector is None:
            def selector(elemento):
                return elemento
        n = len(self.__datos)
        suma = 0.0
        for i in range(n):
            elemento = selector(self.__datos[i])
            if type(elemento) == int or type(elemento) == float:
                suma += elemento
            else:
                raise "Solo podemos trabajar con valores numéricos"
        return suma

    def encontrar_primero(self, predicado: Callable[..., bool]) -> Optional[T]:
        """
        Obtiene el primer elemento de la lista que cumple con el predicado
        :param predicado: el predicado a aplicar a cada elemento de la lista
        :return: el primer elemento de la lista que cumple con el predicado o None si no hay ninguno
        """
        for elemento in self.__datos:
            if predicado(elemento):
                return elemento
        return None

    def encontrar_ultimo(self, predicado: Callable[..., bool]) -> Optional[T]:
        """
        Obtiene el último elemento de la lista que cumple con el predicado
        :param predicado: el predicado a aplicar a cada elemento de la lista
        :return: el último elemento de la lista que cumple con el predicado o None si no hay ninguno
        """
        for elemento in reversed(self.__datos):
            if predicado(elemento):
                return elemento
        return None


    def encontrar_posicion_primero(self, predicado: Callable[..., bool]) -> Optional[int]:
        """
        Obtiene la posición del primer elemento de la lista que cumple con el predicado
        :param predicado: el predicado a aplicar a cada elemento de la lista
        :return: la posición del primer elemento de la lista que cumple con el predicado o None si no hay ninguno
        """
        for i in self.indices:
            if predicado(self.__datos[i]):
                return i
        return None


    def encontrar_posicion_ultimo(self, predicado: Callable[..., bool]) -> Optional[int]:
        """
        Obtiene la posición del último elemento de la lista que cumple con el predicado
        :param predicado: el predicado a aplicar a cada elemento de la lista
        :return: la posición del último elemento de la lista que cumple con el predicado o None si no hay ninguno
        """
        pos_ultimo = None
        for i in self.indices:
            if predicado(self.__datos[i]):
                pos_ultimo = i
        return pos_ultimo


    def mayor(self, menor_que: Callable[..., bool] = None) -> Optional[T]:
        """
        Obtiene el mayor elemento de la lista
        :return: el elemento más grande de la lista. El objeto debe tener definido el operador <
        """
        if len(self.__datos) == 0:
            return None
        if menor_que is None:
            def menor_que(elemento1: T, elemento2: T) -> bool:
                return elemento1 < elemento2
        mayor = self.__datos[0]
        for elemento in self.__datos:
            if menor_que(mayor, elemento):
                mayor = elemento
        return mayor


    def menor(self, menor_que: Callable[..., bool] = None) -> Optional[T]:
        """
        Obtiene y retorna el menor elemento de la lista
        :return: el elemento más pequeño de la lista. El objeto debe tener definido el operador <
        """
        if len(self.__datos) == 0:
            return None
        if menor_que is None:
            def menor_que(elemento1: T, elemento2: T) -> bool:
                return elemento1 < elemento2
        menor = self.__datos[0]
        for elemento in self.__datos:
            if menor_que(elemento, menor):
                menor = elemento
        return menor



    def promedio(self, selector: Callable[..., R] = None) -> float:
        """
        Halla el promedio de los elementos de la lista de acuerdo al selector escogido
        :param selector: la operación a realizar sobre cada elemento de la lista. Si no se especifica, se
                         tomará el valor del elemento.
        :return: el promedio de los elementos de la lista
        """
        if len(self.__datos) == 0:
            return 0.0
        if selector is None:
            def selector(elemento):
                return elemento
        n = len(self.__datos)
        suma = 0.0
        for i in range(n):
            elemento = selector(self.__datos[i])
            if type(elemento) == int or type(elemento) == float:
                suma += elemento
            else:
                raise "Solo podemos trabajar con valores numéricos"
        return suma / n


    def contar(self, predicado: Callable[..., bool] = None) -> int:
        """
        Retorna la cantidad de elementos que cumplen con el predicado en la lista
        :param predicado: el predicado a aplicar a cada elemento de la lista
        :return: la cantidad de elementos que cumplen con el predicado
        """
        if predicado is None:
            return self.tam

        cont = 0
        for elemento in self.__datos:
            if predicado(elemento):
                cont += 1
        return cont


    def porcentaje(self, predicado: Callable[..., bool] = None) -> float:
        """
        Retorna el porcentaje de elementos en la lista que cumplen con el predicado
        :param predicado: el predicado a aplicar a cada elemento de la lista
        :return: el porcentaje de elementos que cumplen con el predicado
        """
        if predicado is None:
            return 100.0

        cont = 0
        for elemento in self.__datos:
            if predicado(elemento):
                cont += 1
        return 0.0 if cont == 0 else 100.0 * cont / len(self.__datos)


    def ordenar(self, menor_que: Callable[..., bool] = None) -> 'Lista[T]':
        """
        Este método ordena la lista de acuerdo a lo que indique el parámetro
        :param menor_que: indica el criterio de comparación de los elementos de la lista.
        :return: la nueva lista ordenada, por el criterio dado.
        """
        lista = copiar_lista(self)
        if menor_que is None:
            def menor_que(elemento1: T, elemento2: T) -> bool:
                return elemento1 < elemento2

        for i in range(lista.tam - 1):
            for j in range(i + 1, lista.tam):
                if menor_que(lista[j], lista[i]):
                    lista[i], lista[j] = lista[j], lista[i]

        return lista


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


def copiar_lista(lista: Lista[T], inicio = 0, fin = None) -> Lista[T]:
    """
    Obtiene una copia idéntica de la lista que se recibe como
    parámetro.
    :param lista: la lista con la que trabajamos
    :return: una copia de la lista
    """
    resultado = Lista[T]()
    ini = inicio
    final = lista.tam if fin is None else fin
    if ini >= final:
        raise "Imposible realizar la copia"
    for indice in range(ini, final):
        elemento = lista[indice]
        resultado.agregar(elemento)
    return resultado

# ---------------------------------------------------------------------

class Node(Generic[T]):
    """"
    Este es un nodo de la lista que se usará para guardar datos en la pila
    """
    def __init__(self, value: T):
        self.info = value
        self.siguiente = None


class Pila(Generic[T]):
    """
    Una pila es una estructura de datos que sigue la filosofía de
    LIFO, el primero que entra es el último en salir.
    """

    # Constructor
    def __init__(self):
        self.__cabeza = None

    # Agregar un elemento
    def apilar(self, elem: T) -> None:
        nodo = Node(elem)
        nodo.siguiente = self.__cabeza
        self.__cabeza = nodo


    # Elimina el primer elemento de la pila
    def desapilar(self) -> None:
        if self.__cabeza is None:
            raise IndexError
        self.__cabeza = self.__cabeza.siguiente


    # Obtiene el primer elemento de la pila
    @property
    def tope(self) -> T:
        if self.__cabeza is None:
            raise IndexError
        return self.__cabeza.info
    

    # Permite saber si la pila está vacía
    @property
    def vacia(self) -> bool:
        return self.__cabeza is None

    # Crea una copia de la pila
    def copiar(self) -> "Pila[T]":
        copia = Pila[T]()
        act = self.__cabeza
        act_copia = None
        while act:
            nodo = Node(act.info)
            if copia.__cabeza is None:
                copia.__cabeza = nodo
                act_copia = nodo
            else:
                act_copia.siguiente = nodo
                act_copia = nodo
            act = act.siguiente
        return copia
    

    # Representación como str de la pila
    def __str__(self):
        act = self.__cabeza
        out = ""
        while act:
            out += str(act.info) + " -> "
            act = act.siguiente
        return out if len(out) == 0 else out[:-4]
    

# ---------------------------------------------------------------------
def crear_pila(*elementos: T) -> Pila[T]:
    """
    Permite crear una pila con los elementos recibidos como parámetro
    :param elementos: los datos a guardar en la pila
    :return: La nueva pila con los elementos recibidos
    """
    resultado = Pila[T]()
    for elemento in elementos:
        resultado.apilar(elemento)
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
        nombre = row["Nombres"].upper()
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

@dataclass(frozen=True)
class EquipoFutbol:
    """Atributos"""
    año: int
    nombre: str
    partidos_ganados_local: int
    partidos_ganados_visitante: int
    partidos_perdidos_local: int
    partidos_perdidos_visitante: int
    partidos_empatados: int
    goles_local: int
    goles_visitante: int
    goles_en_contra: int 


# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Municipio:
    """
    Esta es la información de un municipio de Colombia
    """
    codigo: int
    nombre: str
    poblacion_urbana: int
    poblacion_rural: int
    departamento: str
    es_capital: bool 

    def poblacion_total(self) -> int:
        return self.poblacion_rural + self.poblacion_urbana


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

def leer_archivo_equipos() -> Lista[EquipoFutbol]:
    """
    Permite obtener una lista con la información de los equipos de fútbol de la liga
    :return: la lista de equipos de futbol
    """
    archivo = "https://raw.githubusercontent.com/luiscobo/poo/refs/heads/main/LaLiga.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    lista = Lista[EquipoFutbol]()
    for index, row in df.iterrows():
        año = int(row["season"][:4])
        nombre = row["club"]
        partidos_ganados_local = int(row["home_win"])
        partidos_ganados_visitante = int(row["away_win"])
        partidos_perdidos_local = int(row["home_loss"])
        partidos_perdidos_visitante = int(row["away_loss"])
        partidos_empatados = int(row["matches_drawn"])
        goles_local = int(row["home_goals"])
        goles_visitante = int(row["away_goals"])
        goles_en_contra = int(row["goals_conceded"])
        e = EquipoFutbol(año, nombre, partidos_ganados_local, partidos_ganados_visitante,
                         partidos_perdidos_local, partidos_perdidos_visitante,
                         partidos_empatados, goles_local, goles_visitante,
                         goles_en_contra)
        lista.agregar(e)
    return lista

# ---------------------------------------------------------------------

def leer_archivo_municipios() -> Lista[Municipio]:
    """
    Permite obtener una lista con la información de los municipios de 
    :return: la lista de equipos de futbol
    """
    archivo = "https://raw.githubusercontent.com/luiscobo/poo/refs/heads/main/municipios.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    lista = Lista[Municipio]()
    for index, row in df.iterrows():
        codigo = int(row["código"])
        nombre = row["nombre"]
        poblacion_urbana = int(row["poblaciónUrbana"])
        poblacion_rural = int(row["poblaciónRural"])
        departamento = row["departamento"]
        es_capital = int(row["esCapital"]) == 1
        m = Municipio(codigo=codigo, nombre=nombre, poblacion_rural=poblacion_rural,
                      poblacion_urbana=poblacion_urbana, departamento=departamento,
                      es_capital=es_capital)
        lista.agregar(m)
    return lista


# ---------------------------------------------------------------------

def pila_municipios() -> Pila[Municipio]:
    """
    Permite obtener una pila con la información de los municipios de 
    :return: la lista de equipos de futbol
    """
    archivo = "https://raw.githubusercontent.com/luiscobo/poo/refs/heads/main/municipios.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    pila = Pila[Municipio]()
    for index, row in df.iterrows():
        codigo = int(row["código"])
        nombre = row["nombre"]
        poblacion_urbana = int(row["poblaciónUrbana"])
        poblacion_rural = int(row["poblaciónRural"])
        departamento = row["departamento"]
        es_capital = int(row["esCapital"]) == 1
        m = Municipio(codigo=codigo, nombre=nombre, poblacion_rural=poblacion_rural,
                      poblacion_urbana=poblacion_urbana, departamento=departamento,
                      es_capital=es_capital)
        pila.apilar(m)
    return pila


# ---------------------------------------------------------------------
from io import StringIO
import shlex

def dividir_expresion(expresion: str) -> Lista[str]:
    """
    Esta función toma una expresión y obtiene los
    diferentes tokens que hacen parte de ella
    """
    inp = StringIO(expresion)
    res = Lista[str]()
    for elem in list(shlex.shlex(inp)):
        res.agregar(elem)
    return res


# ---------------------------------------------------------------------
# Funciones auxiliares

def elevar(x: int, y: int) -> int:
    return int(int(x) ** int(y))


# ---------------------------------------------------------------------

class NodoArbin(Generic[T]):
    """"
    Este es un nodo de un árbol binario genérico
    """
    def __init__(self, info: T, izq: Optional["NodoArbin"] = None, der: Optional["NodoArbin"] = None):
        self.info = info
        self.izq = izq
        self.der = der


    def es_hoja(self) -> bool:
        """
        Permite saber si este árbol es una hoja o no
        :return: true si el nodo no tiene hijos, y false en caso contrario
        """
        return self.izq is None and self.der is None


def arbol_de_letras() -> NodoArbin[str]:
    """
    Permite crear un árbol de letras mayúsculas
    :return:
    """
    return NodoArbin(
        "A",
        NodoArbin(
            "B",
            NodoArbin(
                "D",
                NodoArbin("G")
            ),
            NodoArbin(
                "E",
                NodoArbin("H"),
                NodoArbin("I")
            )
        ),
        NodoArbin(
            "C",
            None,
            NodoArbin(
                "F",
                NodoArbin(
                    "J",
                    None,
                    NodoArbin("K")
                )
            )
        )
    )


def arbol_de_numeros() -> NodoArbin[int]:
    return NodoArbin(
        60,
        NodoArbin(
            41,
            NodoArbin(
                16,
                None,
                NodoArbin(25)
            ),
            NodoArbin(
                53,
                NodoArbin(
                    46,
                    NodoArbin(42)
                ),
                NodoArbin(55)
            )
        ),
        NodoArbin(
            74,
            NodoArbin(
                65,
                NodoArbin(
                    63,
                    NodoArbin(62),
                    NodoArbin(64)
                ),
                NodoArbin(70)
            )
        )
    )


def crear_arbol_de_lista(lista: Lista[T]) -> NodoArbin[T]:
    """
    Crea un árbol binario a partir de una lista
    :param lista: la lista con los objetos
    :return: el arbol binario
    """
    def crear_arbol_aux(lista: Lista[T], posicion: int) -> Optional[NodoArbin[T]]:
        tam = lista.tam
        if posicion >= tam:
            return None
        act = NodoArbin(lista[posicion])
        pos_izq = 2 * posicion + 1
        pos_der = 2 * posicion + 2
        if pos_izq < tam:
            act.izq = crear_arbol_aux(lista, pos_izq)
        if pos_der < tam:
            act.der = crear_arbol_aux(lista, pos_der)
        return act

    # ------------------------------------------------------------------------------
    return crear_arbol_aux(lista, 0)


def arbol_verbos() -> NodoArbin[str]:
    """
    Crea un árbol binario con verbos a partir de una lista
    :return: el árbol binario con verbos
    """
    verbos = crear_lista("comer",
        "cenar", "partir", "tener", "sufrir",
        "internacionalizar", "exponer", "pedir",
        "sanar", "mecer", "adolecer")
    return crear_arbol_de_lista(verbos)


def arbol_personas() -> NodoArbin[Persona]:
    return  crear_arbol_de_lista(leer_archivo_personas())


# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Punto:
    """
    Esta clase representa un punto en el plano cartesiano
    """
    x: float
    y: float

    @property
    def radio(self) -> float:
        """
        Obtiene la distancia al origen del punto
        :return: la distancia al origen del punto
        """
        return sqrt(self.x ** 2 + self.y ** 2)


    def distancia_al_origen(self) -> float:
        return self.radio


    @property
    def angulo(self) -> float:
        """
        Retorna el angulo con el eje x del punto
        :return: el ángulo
        """
        return math.atan2(self.y, self.x)


    def cuadrante(self) -> int:
        """
        Obtener el cuadrante al que pertenece el punto
        :return: 1, 2, 3 o 4 dependiendo del cuadrante al que pertenece el punto
        """
        if self.x >= 0:
            if self.y >= 0:
                return 1
            else:
                return 4
        else:
            if self.y >= 0:
                return 2
            else:
                return 3


def lista_de_puntos() -> Lista[Punto]:
    return crear_lista(
        Punto(15.0, -10.0),
        Punto(5.0, 4.0),
        Punto(-3.0, 15.0),
        Punto(-8.0, -30.0),
        Punto(-7.0, 25.0),
        Punto(6.0, -70.0),
        Punto(9.0, 10.0),
        Punto(-8.0, -61.0),
        Punto(90.0, -80.0),
        Punto(-75.0, -80.0),
        Punto(45.0, -77.0),
        Punto(3.0, 4.0)
    )


def arbol_de_puntos() -> NodoArbin[Punto]:
    return crear_arbol_de_lista(lista_de_puntos())


# ---------------------------------------------------------------------

# Otros árboles
def arbol_de_departamentos() -> NodoArbin[Departamento]:
    return crear_arbol_de_lista(leer_archivo_departamentos())

def arbol_de_equipos() -> NodoArbin[EquipoFutbol]:
    return crear_arbol_de_lista(leer_archivo_equipos())

def arbol_de_municipios() -> NodoArbin[Municipio]:
    return crear_arbol_de_lista(leer_archivo_municipios())

# ---------------------------------------------------------------------

@dataclass(frozen=True)
class Producto:
    codigo: int
    categoria: int
    nombre: str
    modelo: str
    descripcion: str
    color: str
    costo: float
    precio: float


    def ganancia(self) -> float:
        """
        Obtiene la ganancia de un producto
        :return: la diferencia entre el precio y el costo
        """
        return self.precio - self.costo


def lista_de_productos() -> Lista[Producto]:
    """
    Permite obtener una lista con la información de los productos
    :return: la lista de productos del archivo
    """
    archivo = "https://raw.githubusercontent.com/luiscobo/poo/refs/heads/main/Product.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    lista = Lista[Producto]()
    for index, row in df.iterrows():
        codigo = int(row["ProductKey"])
        categoria = int(row["ProductSubcategoryKey"])
        nombre = row["ProductName"]
        modelo = row["ModelName"]
        descripcion = row["ProductDescription"]
        color = row["ProductColor"]
        costo = float(row["ProductCost"])
        precio = float(row["ProductPrice"])
        prod = Producto(codigo, categoria, nombre, modelo, descripcion, color, costo, precio)
        lista.agregar(prod)
    return lista


def arbol_de_productos() -> NodoArbin[Producto]:
    return crear_arbol_de_lista(lista_de_productos())

# ----------------------------------------------------------------------

@dataclass(frozen=True)
class Carro:
    codigo: int
    modelo: str
    año: int
    precio: int
    transmision: str
    kilometraje: int
    tipo_combustible: str
    cilindraje: float
    fabricante: str

    def edad(self) -> int:
        """"
        Determina el número de años que ha sido fabricado el carro
        """
        hoy = datetime.now()
        anio = hoy.year
        return anio - self.año


def lista_de_carros_usados(n: int = 10) -> Lista[Carro]:
    """
    Permite obtener una lista con la información de los carros
    :return: la lista de carros del archivo
    """
    archivo = "https://raw.githubusercontent.com/luiscobo/poo/refs/heads/main/cars_dataset.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    lista = Lista[Carro]()
    i = 1
    for index, row in df.iterrows():
        modelo = row["model"].upper().strip()
        año = int(row["year"])
        precio = int(row["price"])
        transmision = "MANUAL" if row["transmission"] == "Manual" else "AUTOMATICA" if row["transmission"] == "Automatic" else "SEMIAUTOMATICA"
        kilometraje = int(row["mileage"])
        tipo_combustible = "GASOLINA" if row["fuelType"] == "Petrol" else "ACPM" if row["fuelType"] == "Diesel" else "ELECTRICO"
        cilindraje = float(row["engineSize"])
        fabricante = row["Make"].upper()
        carro = Carro(i, modelo, año, precio, transmision, kilometraje, tipo_combustible, cilindraje, fabricante)
        lista.agregar(carro)
        i += 1
        if i > n:
            break
    return lista

# ---------------------------------------------------------------------

def es_menor_que(objeto1, objeto2, atributos: str = None) -> bool:
    """
    Permite saber si el objeto1 es mas pequeño que el objeto2 de acuerdo a los atributos
    :param objeto1: el primer objeto
    :param objeto2: el segundo objeto
    :param atributos: un string con los nombres de los atributos de la clase
    :return: True si el objeto1 < objeto2, False si no
    """
    if type(objeto1) != type(objeto2):
        return False
    if atributos is None:
        return objeto1 < objeto2
    else:
        nombre_attrs = [atrib.strip() for atrib in atributos.split(",")]
        for nombre_attr in nombre_attrs:
            if nombre_attr.endswith(")"):
                nomatrib = nombre_attr.split("(")[0].strip()
            else:
                nomatrib = nombre_attr
            if not hasattr(objeto1, nomatrib):
                raise f"El objeto no tiene el atributo {nomatrib}"
            if not hasattr(objeto2, nomatrib):
                raise f"El objeto no tiene el atributo {nomatrib}"
            if nombre_attr.endswith(")"):
                valor1 = getattr(objeto1, nomatrib)()
                valor2 = getattr(objeto2, nomatrib)()
            else:
                valor1 = getattr(objeto1, nomatrib)
                valor2 = getattr(objeto2, nomatrib)
            if valor1 < valor2:
                return True
            if valor1 > valor2:
                return False
        return False  # Son iguales


def son_iguales(objeto1, objeto2, atributos: str = None) -> bool:
    """
    Permite saber si el objeto1 es igual que el objeto2 de acuerdo a los atributos
    :param objeto1: el primer objeto
    :param objeto2: el objeto 2
    :param atributos: una lista de atributos y métotdos usados como criterios de comparación
    :return: True si el objeto1 es igual a la objeto 2 de acuedo con los atributos.
    """
    if type(objeto1) != type(objeto2):
        return False
    if atributos is None:
        return objeto1 == objeto2
    else:
        nombre_attrs = [atrib.strip() for atrib in atributos.split(",")]
        for nombre_attr in nombre_attrs:
            if nombre_attr.endswith(")"):
                nomatrib = nombre_attr.split("(")[0].strip()
            else:
                nomatrib = nombre_attr
            if not hasattr(objeto1, nomatrib):
                raise f"El objeto no tiene el atributo {nomatrib}"
            if not hasattr(objeto2, nomatrib):
                raise f"El objeto no tiene el atributo {nomatrib}"
            if nombre_attr.endswith(")"):
                valor1 = getattr(objeto1, nomatrib)()
                valor2 = getattr(objeto2, nomatrib)()
            else:
                valor1 = getattr(objeto1, nomatrib)
                valor2 = getattr(objeto2, nomatrib)
            if valor1 != valor2:
                return False

        return True  # Son iguales


if __name__ == '__main__':
    lc = lista_de_carros_usados()
    print(lc.tam)
    print(lc[0])
    print(lc[1].edad())

