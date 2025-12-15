import sys
import os
import unittest

# Ensure src is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from siirto import Siirto
from tekoaly import YksinkertainenTekoaly, KehittynytTekoaly


class TestTekoaly(unittest.TestCase):
    def test_yksinkertainen_cycles(self):
        ai = YksinkertainenTekoaly()  # starts with KIVI
        first = ai.anna_siirto()
        second = ai.anna_siirto()
        third = ai.anna_siirto()
        self.assertEqual(first, Siirto.SAKSET)
        self.assertEqual(second, Siirto.PAPERI)
        self.assertEqual(third, Siirto.KIVI)

    def test_kehittynyt_memory_choice(self):
        ai = KehittynytTekoaly(10)
        # When memory empty, anna_siirto may be random; seed memory instead
        ai.lisaa_siirto(Siirto.SAKSET)
        ai.lisaa_siirto(Siirto.SAKSET)
        ai.lisaa_siirto(Siirto.KIVI)
        # Most common is SAKSET (value 2) so anna_siirto should choose the move that beats SAKSET
        next_move = ai.anna_siirto()
        # Compute expected: for suosituin value 2 -> ((2 + 1) % 3) + 1 => ((3) % 3) + 1 = 0 + 1 = 1 => KIVI
        self.assertEqual(next_move, Siirto.KIVI)


if __name__ == '__main__':
    unittest.main()
