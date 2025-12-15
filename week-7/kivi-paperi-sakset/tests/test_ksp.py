import sys
import os
import unittest

# Ensure src is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from siirto import Siirto
from ksp import KspPelaajaVsPelaaja, KspYksinkertainenTekoaly, KspKehittynytTekoaly


class TestKsp(unittest.TestCase):
    def test_pvp_pelaa_siirrot_updates_score(self):
        game = KspPelaajaVsPelaaja()
        # Kivi vs Sakset -> ensimmäinen should win
        result = game.pelaa_siirrot(Siirto.KIVI, Siirto.SAKSET)
        self.assertIn('Pelitilanne', result)
        self.assertEqual(game.tuomari.ekan_pisteet, 1)
        self.assertEqual(game.tuomari.tokan_pisteet, 0)

    def test_simple_ai_pelaa_eka(self):
        game = KspYksinkertainenTekoaly()
        # Simple AI cycles: starting KIVI -> AI returns SAKSET on first call
        toka, tuomari_str = game.pelaa_eka(Siirto.KIVI)
        self.assertEqual(toka, Siirto.SAKSET)
        # Kivi vs Sakset -> first player wins
        self.assertEqual(game.tuomari.ekan_pisteet, 1)

    def test_advanced_ai_with_memory(self):
        game = KspKehittynytTekoaly()
        # seed AI memory directly
        game.tekoaly.lisaa_siirto(Siirto.SAKSET)
        game.tekoaly.lisaa_siirto(Siirto.SAKSET)
        game.tekoaly.lisaa_siirto(Siirto.KIVI)
        # Now play: provide a move for first player
        toka, _ = game.pelaa_eka(Siirto.KIVI)
        # With most common SAKSET, advanced ai should choose KIVI (see algorithm)
        self.assertEqual(toka, Siirto.KIVI)

    def test_game_ends_at_five_pvp(self):
        game = KspPelaajaVsPelaaja()
        # First player wins 3 times
        for _ in range(3):
            game.pelaa_siirrot(Siirto.KIVI, Siirto.SAKSET)
        self.assertEqual(game.tuomari.ekan_pisteet, 3)
        # further submits should have no effect
        game.pelaa_siirrot(Siirto.KIVI, Siirto.SAKSET)
        self.assertEqual(game.tuomari.ekan_pisteet, 3)

    def test_game_ends_at_five_ai(self):
        game = KspYksinkertainenTekoaly()
        # simulate end state by setting points directly
        game.tuomari.ekan_pisteet = 3
        # calling pelaa_eka should have no effect
        before = (game.tuomari.ekan_pisteet, game.tuomari.tokan_pisteet)
        game.pelaa_eka(Siirto.KIVI)
        after = (game.tuomari.ekan_pisteet, game.tuomari.tokan_pisteet)
        self.assertEqual(before, after)


if __name__ == '__main__':
    unittest.main()
