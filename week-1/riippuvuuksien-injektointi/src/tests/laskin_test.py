import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs if inputs else []
        self.outputs = []

    def lue(self, teksti):
        print(self.inputs)
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)

    def lisaa_syote(self, teksi):
        self.inputs.append(teksti)


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 4")

    def test_kaksi_summaa_oikein(self):
        io = StubIO(["1", "3", "6", "10", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()
        tulos_1 = io.outputs[0]
        tulos_2 = io.outputs[1]

        self.assertEqual(f"{tulos_1} {tulos_2}", "Summa: 4 Summa: 16")
