# Pruebas
import unittest
from __main__ import Materia, Estudiante

# ---------------------------------------------------

class TestEstudiante(unittest.TestCase):
    def setUp(self):
        mat1 = Materia('Astronomia', 10, 30, 95, 95, 0.0, False, False, False)
        mat2 = Materia('Astrofisica', 40, 87, 0, 0, 0, True, False, False)
        mat3 = Materia('Emprendimiento', 66, 71, 88, 72, 30, False, True, False)
        mat4 = Materia('Calculo', 95, 100, 0, 0, 98, True, True, False)
        mat5 = Materia('Historia', 55, 19, 98, 100, 0, False, False, True)
        mat6 = Materia('Biologia', 76, 10, 20, 30, 0, False, False, False)
        self.est = Estudiante('Pedro Perez', mat1, mat2, mat3, mat4, mat5, mat6)
        self.est2 = Estudiante('Carlos Castro', mat4, mat4, mat4, mat4, mat4, mat4)
        mat7 = Materia('Astrologia', 90, 10, 0, 0, 0, True, False, False)
        self.est3 = Estudiante("Tomas Torres", mat2, mat7, mat6, mat6, mat6, mat6)


    def test_cant_mat_perdidas(self):
        self.assertEqual(1, self.est.cant_mat_perdidas())


    def test_promedio(self):
        self.assertAlmostEqual(68.1, self.est.promedio(), places=1)


    def test_cant_mat_aprobadas(self):
        self.assertEqual(5, self.est.cant_mat_aprobadas())


    def test_aprobo_todas(self):
        self.assertFalse(self.est.aprobo_todas())
        self.assertTrue(self.est2.aprobo_todas())


    def test_nota_mas_alta(self):
        self.assertEqual('Calculo', self.est.nota_mas_alta())


    def test_nota_mas_baja(self):
        mat = self.est.mat_nota_mas_baja()
        self.assertEqual(mat, self.est.mat6)


    def test_suma_primer_corte_mats_ciclo(self):
        self.assertEqual(40.0, self.est.suma_primer_corte_mats_ciclo('Astro'))
        self.assertEqual(0.0, self.est.suma_primer_corte_mats_ciclo('Bio'))
        self.assertEqual(130.0, self.est3.suma_primer_corte_mats_ciclo('Astro'))
        self.assertEqual(0.0, self.est.suma_primer_corte_mats_ciclo('Mate'))


    def test_materia_con_nombre(self):
        self.assertEqual(self.est.mat1, self.est.materia_con_nombre('Astronomia'))
        self.assertIsNone(self.est.materia_con_nombre('Geografia'))
        self.assertEqual(self.est3.mat2, self.est3.materia_con_nombre('Astrologia'))

    
    def test_aprobo_con_mal_comienzo(self):
        self.assertTrue(self.est.aprobo_con_mal_comienzo('Astronomia'))
        self.assertTrue(self.est.aprobo_con_mal_comienzo('Historia'))
        self.assertFalse(self.est.aprobo_con_mal_comienzo('Biologia'))

    
    def test_cant_mats_primer_corte(self):
        self.assertEqual(1, self.est.cant_mats_pimer_corte(80))
        self.assertEqual(3, self.est.cant_mats_pimer_corte(60))
        self.assertEqual(6, self.est.cant_mats_pimer_corte(10))


# ------------------------------------------------------------------------
