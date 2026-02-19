import unittest
from logica_liq_nom import calcular_nomina

class TestNomina(unittest.TestCase):

    def test_caso_normal(self):
        # Caso: 1.5M, 30 días, 2 extras diurnas...
        resultado = calcular_nomina(1500000, 30, 0, 2, "D", 162000, 0, 0)
        self.assertIn("Neto a Pagar", resultado)
        self.assertGreater(resultado["Neto a Pagar"], 0)

    def test_incapacidad_total(self):
        # Caso: 1.8M, 0 días trab, 30 días incapacidad
        resultado = calcular_nomina(1800000, 0, 30, 0, "D", 0, 0, 0)
        # El devengado debería ser el 66% del salario base
        esperado_devengado = 1800000 * 0.66
        self.assertAlmostEqual(resultado["Total Devengado"], esperado_devengado)

    def test_salario_negativo_error(self):
        # Verifica que se lance la excepción ValueError
        with self.assertRaises(ValueError) as context:
            calcular_nomina(-1500000, 30, 0, 5, "D", 162000, 0, 0)
        self.assertEqual(str(context.exception), "El salario no puede ser negativo")

    def test_exceso_dias_error(self):
        with self.assertRaises(ValueError):
            # 31 días trabajados supera el límite
            calcular_nomina(1500000, 31, 0, 0, "D", 0, 0, 0)

    def test_horas_extra_negativas_error(self):
        with self.assertRaises(ValueError):
            calcular_nomina(1500000, 30, 0, -4, "D", 162000, 0, 0)

if __name__ == "__main__":
    unittest.main()