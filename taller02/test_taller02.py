# Estas son las pruebas de la clase producto
import unittest

# Casos de prueba
class TestProducto(unittest.TestCase):

    def setUp(self):
        """Configuración de los objetos que vamos a usar en las pruebas"""
        self.lapiz = Producto("lapiz", "papeleria", 550, 18, 5)
        self.aspirina = Producto("aspirina", "drogueria", 109.5, 25, 8)
        self.pan = Producto("pan", "supermercado", 150.0, 15, 20)

    def test_constructor_getters(self):
        """Prueba del constructor de la clase producto"""
        self.prod = Producto("cuaderno", "papeleria", 300.0, 5, 2)
        self.assertEqual(self.prod.dar_nombre(), "cuaderno")
        self.assertEqual(self.prod.dar_tipo(), "papeleria")
        self.assertEqual(self.prod.dar_cantidad_bodega(), 5)
        self.assertEqual(self.prod.dar_cantidad_minima(), 2)
        self.assertEqual(self.prod.dar_valor_unitario(), 300.0)
        self.assertEqual(self.prod.dar_cantidad_unidades_vendidas(), 0)

    def test_dar_precio_final(self):
        """Prueba del método de dar el precio final de un producto"""
        lapiz = self.lapiz
        aspirina = self.aspirina
        pan = self.pan
        # -----
        self.assertAlmostEqual(638.0, lapiz.dar_precio_final(), places=1)
        self.assertAlmostEqual(122.64, aspirina.dar_precio_final(), places=2)
        self.assertAlmostEqual(156.0, pan.dar_precio_final(), places=1)


    def test_vender(self):
        """Prueba del método vender de la clase producto"""
        self.assertEqual(18, self.lapiz.dar_cantidad_bodega())
        resultado = self.lapiz.vender(10)
        self.assertEqual(8, self.lapiz.dar_cantidad_bodega())
        self.assertEqual(10, resultado)
        self.assertEqual(638.0, self.lapiz.dar_precio_final())
        self.assertEqual(10, self.lapiz.dar_cantidad_unidades_vendidas())

        resultado = self.lapiz.vender(30)
        self.assertEqual(0, self.lapiz.dar_cantidad_bodega())
        self.assertEqual(8, resultado)
        self.assertEqual(638.0, self.lapiz.dar_precio_final())
        self.assertEqual(18, self.lapiz.dar_cantidad_unidades_vendidas())

        self.assertEqual(15, self.pan.dar_cantidad_bodega())
        resultado = self.pan.vender(5)
        self.assertEqual(10, self.pan.dar_cantidad_bodega())
        self.assertEqual(5, self.pan.dar_cantidad_unidades_vendidas())
        resultado = self.pan.vender(5)
        self.assertEqual(5, self.pan.dar_cantidad_bodega())
        self.assertEqual(10, self.pan.dar_cantidad_unidades_vendidas())


    def test_abastecer(self):
        """Prueba del método abastecer de la clase Producto"""
        self.assertEqual(18, self.lapiz.dar_cantidad_bodega())
        resultado = self.lapiz.abastecer(15)
        self.assertEqual(33, self.lapiz.dar_cantidad_bodega())
        self.assertEqual(5, self.lapiz.dar_cantidad_minima())
        self.assertEqual(33, resultado)

        resultado = self.lapiz.abastecer(-10)
        self.assertEqual(33, resultado)
        self.assertEqual(33, self.lapiz.dar_cantidad_bodega())

        resultado = self.lapiz.abastecer(17)
        self.assertEqual(50, resultado)
        self.assertEqual(50, self.lapiz.dar_cantidad_bodega())


    def test_puede_abastecer(self):
        """Prueba del método puede_abastecer de la clase producto"""
        self.assertFalse(self.lapiz.puede_abastecer())
        self.assertFalse(self.aspirina.puede_abastecer())
        self.assertTrue(self.pan.puede_abastecer())


# ----------------------------------------
# Aquí se ejecutan los casos de prueba
def probar_clase_producto():
    unittest.main(argv=['', '-v', 'TestProducto'], verbosity=2, exit=False)
