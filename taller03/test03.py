# Pruebas
import unittest
from __main__ import Materia

# Casos de prueba
class PruebaClaseEstudiante(unittest.TestCase):
    
    # Probar la nota definitiva
    def test_definitiva(self):
        materia = Materia("Calculo", 40.0, 55.0, 32.0, 80.0, 0.0, es_de_ciclo=False, tiene_pruebas_objetivas=False, es_de_postgrado=False)
        self.assertAlmostEqual(52.6, materia.definitiva(), places=1)

        materia.tiene_pruebas_objetivas = True
        self.assertAlmostEqual(44.6, materia.definitiva(), places=1)

        materia.pruebas_objetivas = 75.0
        self.assertAlmostEqual(52.1, materia.definitiva(), places=1)

        materia.es_de_ciclo = True
        self.assertAlmostEqual(51.0, materia.definitiva(), places=1)

        materia.tiene_pruebas_objetivas = False
        self.assertAlmostEqual(49.0, materia.definitiva(), places=1)

        mat = Materia('Física', 65.0, 75.0, 0.0, 0.0, 0.0, es_de_ciclo=True, tiene_pruebas_objetivas=False, es_de_postgrado=False)
        self.assertAlmostEqual(71.0, mat.definitiva(), places=1)

    # Probar si aprobo o no
    def test_aprobo(self):
        mat1 = Materia('Química', 77.0, 81.0, 0.0, 0.0, 0.0, es_de_ciclo=True, tiene_pruebas_objetivas=False, es_de_postgrado=False)
        self.assertTrue(mat1.aprobo())

        mat2 = Materia('Emprendimiento', 65.0, 61.0, 66.0, 70.0, 0.0, es_de_ciclo=False, tiene_pruebas_objetivas=False, es_de_postgrado=True)
        self.assertFalse(mat2.aprobo())
        mat2.es_de_postgrado = False
        self.assertTrue(mat2.aprobo())

        mat3 = Materia('Filosofía', 90.0, 95.0, 0.0, 0.0, 0.0, True, False, True)
        self.assertTrue(mat3.aprobo())


# ---------------------------------------------------
# Ejecución de los casos de prueba
def prueba_clase_estudiante() -> None:
    unittest.main(argv=['', '-v', 'PruebaClaseEstudiante'], verbosity=2, exit=False)
