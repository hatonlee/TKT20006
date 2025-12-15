from siirto import Siirto

class Tuomari:
    def __init__(self) -> None:
        self.ekan_siirrot = []
        self.tokan_siirrot = []
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_piste(self, eka: Siirto, toka: Siirto) -> None:
        self._kirjaa_siirrot(eka, toka)
        self.ekan_pisteet += int(self._voittaa(eka, toka))
        self.tokan_pisteet += int(self._voittaa(toka, eka))
        self.tasapelit += int(self._tasapeli(eka, toka))

    def __str__(self) -> str:
        return f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\nTasapelit: {self.tasapelit}"

    def _tasapeli(self, eka: Siirto, toka: Siirto) -> bool:
        return eka == toka

    def _voittaa(self, eka: Siirto, toka: Siirto) -> bool:
        return toka.value == eka.value % 3 + 1

    def _kirjaa_siirrot(self, eka: Siirto, toka: Siirto) -> None:
        self.ekan_siirrot.append(eka)
        self.tokan_siirrot.append(toka)
