# Ejemplo

from __main__ import sumar

def assert_is_true(cond: bool) -> None:
    if cond:
        print('OK')
    else:
        print('FAIL')

def prueba_sumar():
    m = sumar(3, 4)
    assert_is_true(7 == m)
   
