# Ejemplo
import __main__

def assert_is_true(cond: bool) -> None:
    if cond:
        print('OK')
    else:
        print('FAIL')

def prueba_sumar():
    print('Reloaded')
    m = __main__.sumar(3, 4)
    assert_is_true(7 == m)
   
