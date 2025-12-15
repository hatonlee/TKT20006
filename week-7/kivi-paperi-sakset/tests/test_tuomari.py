import sys
import os
import unittest

# Ensure src is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from siirto import Siirto
from tuomari import Tuomari


class TestTuomari(unittest.TestCase):
    def test_initial_state(self):
        t = Tuomari()
        self.assertEqual(t.ekan_siirrot, [])
        self.assertEqual(t.tokan_siirrot, [])
        self.assertEqual(t.ekan_pisteet, 0)
        self.assertEqual(t.tokan_pisteet, 0)
        self.assertEqual(t.tasapelit, 0)

    def test_kirjaa_eka_wins(self):
        t = Tuomari()
        # Kivi vs Sakset -> ensimmäinen should get a point
        t.kirjaa_piste(Siirto.KIVI, Siirto.SAKSET)
        self.assertEqual(t.ekan_pisteet, 1)
        self.assertEqual(t.tokan_pisteet, 0)
        self.assertEqual(t.tasapelit, 0)
        self.assertEqual(t.ekan_siirrot[-1], Siirto.KIVI)
        self.assertEqual(t.tokan_siirrot[-1], Siirto.SAKSET)

    def test_kirjaa_toka_wins(self):
        t = Tuomari()
        # Kivi vs Paperi -> second should get a point
        t.kirjaa_piste(Siirto.KIVI, Siirto.PAPERI)
        self.assertEqual(t.ekan_pisteet, 0)
        self.assertEqual(t.tokan_pisteet, 1)
        self.assertEqual(t.tasapelit, 0)

    def test_tie(self):
        t = Tuomari()
        t.kirjaa_piste(Siirto.SAKSET, Siirto.SAKSET)
        self.assertEqual(t.ekan_pisteet, 0)
        self.assertEqual(t.tokan_pisteet, 0)
        self.assertEqual(t.tasapelit, 1)


if __name__ == '__main__':
    unittest.main()
