import unittest
from logica_liq_nom import calcular_nomina, ResultadoNomina

class TestNomina(unittest.TestCase):

    # ==============================
    # CASOS NORMALES
    # ==============================
    def test_caso_normal_1(self):
        resultado = calcular_nomina(1500000, 30, 2, 10, "D", 162000, 124000, 0)

        self.assertAlmostEqual(resultado.total_devengado, 1930125.0, 2)
        self.assertAlmostEqual(resultado.total_deducciones, 154410.0, 2)
        self.assertAlmostEqual(resultado.neto, 1775715.0, 2)

    def test_caso_normal_2(self):
        resultado = calcular_nomina(2000000, 30, 3, 5, "D", 162000, 140000, 50000)

        self.assertAlmostEqual(resultado.total_devengado, 2486083.3333, 2)
        self.assertAlmostEqual(resultado.total_deducciones, 248886.6667, 2)
        self.assertAlmostEqual(resultado.neto, 2237196.6667, 2)

    def test_caso_normal_3(self):
        resultado = calcular_nomina(1800000, 28, 0, 8, "N", 162000, 50000, 20000)

        self.assertAlmostEqual(resultado.total_devengado, 1997000.0, 2)
        self.assertAlmostEqual(resultado.total_deducciones, 179760.0, 2)
        self.assertAlmostEqual(resultado.neto, 1817240.0, 2)

    # ==============================
    # CASOS EXTRAORDINARIOS
    # ==============================

    def test_sin_horas_extra(self):
            resultado = calcular_nomina(1500000, 30, 0, 0, "D", 162000, 0, 0)

            # salario completo + auxilio
            self.assertAlmostEqual(resultado.total_devengado, 1662000.0, 2)
            self.assertAlmostEqual(resultado.total_deducciones, 132960.0, 2)
            self.assertAlmostEqual(resultado.neto, 1529040.0, 2)
    
    def test_pocos_dias_trabajados(self):
        resultado = calcular_nomina(2000000, 15, 0, 5, "D", 0, 0, 0)

        self.assertAlmostEqual(resultado.total_devengado, 1052083.3333, 2)
        self.assertAlmostEqual(resultado.total_deducciones, 84166.6667, 2)
        self.assertAlmostEqual(resultado.neto, 967916.6667, 2)

    def test_deducciones_muy_altas(self):
        resultado = calcular_nomina(1500000, 30, 0, 0, "D", 162000, 0, 2000000)

        self.assertAlmostEqual(resultado.total_devengado, 1662000.0, 2)
        self.assertAlmostEqual(resultado.total_deducciones, 2132960.0, 2)
        self.assertAlmostEqual(resultado.neto, -470960.0, 2)

    # ==============================
    # CASOS ERROS
    # ==============================

    def test_error_dias_mayores_a_30(self):
        resultado = calcular_nomina(1500000, 35, 3, 5, "D", 162000, 100000, 0)
        self.assertLessEqual(35, 30, "ERROR: los dias trabajados deben ser maximo 30")

    def test_error_salario_negativo(self):
        resultado = calcular_nomina(-1500000, 30, 6, 5, "N", 162000, 500000, 0)
        self.assertGreaterEqual(resultado.total_devengado, 0, "ERROR: el salario no puede ser negativo")

    def test_error_horas_extra_negativas(self):
        resultado = calcular_nomina(1500000, 30, 4, -4, "D", 162000, 111110, 0)
        self.assertGreaterEqual(resultado.total_extras, 0, "ERROR: no se pueden descontar horas")

    def test_error_deducciones_exceden_neto(self):
        resultado = calcular_nomina(1500000, 30, 7, 5, "N", 162000, 5000, 2000000)
        self.assertGreaterEqual(resultado.neto, 0, "ERROR: Las deduciones son mayores al salario neto")


if __name__ == "__main__":
    unittest.main()
