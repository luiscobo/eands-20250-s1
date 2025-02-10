# Ejemplo
import __main__
from __main__ import sumar
import importlib

importlib.reload(__main__)

def assert_is_true(cond: bool) -> None:
    if cond:
        print('OK')
    else:
        print('FAIL')

def prueba_sumar():
    importlib.reload(__main__)
    m = sumar(3, 4)
    assert_is_true(7 == m)
   
