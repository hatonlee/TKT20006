from siirto import Siirto
from collections import deque, Counter
from random import randint

class YksinkertainenTekoaly:
    def __init__(self, alku_siirto: Siirto = Siirto.KIVI):
        self._siirto = alku_siirto.value

    def anna_siirto(self) -> Siirto:
        self._siirto = (self._siirto + 1) % 3
        return Siirto.from_int(self._siirto)


class KehittynytTekoaly:
    def __init__(self, muistin_koko: int):
        self._muisti = deque(maxlen=muistin_koko)

    def anna_siirto(self) -> Siirto:
        if not self._muisti:
            return Siirto.from_int(randint(0, 2))

        suosituin_siirto = Counter(self._muisti).most_common(1)[0][0]
        return Siirto.from_int((suosituin_siirto.value + 1) % 3 + 1)

    def lisaa_siirto(self, siirto: Siirto):
        self._muisti.append(siirto)
