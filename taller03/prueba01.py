# Ejemplo
import __main__
import importlib

def assert_is_true(cond: bool) -> None:
    if cond:
        print('OK')
    else:
        print('FAIL')

def prueba_sumar():
    importlib.reload(__main__)
    print('Reloaded')
    m = __main__.sumar(3, 4)
    assert_is_true(7 == m)
   
