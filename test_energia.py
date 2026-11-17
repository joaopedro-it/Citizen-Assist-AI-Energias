import unittest
from energia import calcular

class TesteEnergia(unittest.TestCase):
    def test_exemplo(self):
        r=calcular(200,5,0.9)
        self.assertAlmostEqual(r['custo_atual_rs_mes'],180)
        self.assertAlmostEqual(r['led']['economia_kwh_mes'],38.25)
        self.assertAlmostEqual(r['solar']['geracao_kwh_mes'],120)
        self.assertAlmostEqual(r['solar']['economia_rs_mes'],108)
    def test_limite_consumo(self):
        r=calcular(10,5,0.9)
        self.assertLessEqual(r['led']['economia_kwh_mes'],10)
        self.assertLessEqual(r['solar']['geracao_kwh_mes'],10)
    def test_invalido(self):
        with self.assertRaises(ValueError): calcular(0)
        with self.assertRaises(ValueError): calcular(200,-1)
if __name__=='__main__': unittest.main()
