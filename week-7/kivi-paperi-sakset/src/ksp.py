from tuomari import Tuomari
from tekoaly import YksinkertainenTekoaly, KehittynytTekoaly
from siirto import Siirto


class KiviSaksetPaperi:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa(self):
        ekan_siirto = self._ensimmainen_siirto()
        tokan_siirto = self._toinen_siirto()
        self.tuomari.kirjaa_piste(ekan_siirto, tokan_siirto)
        print(self.tuomari)

    def _ensimmainen_siirto(self) -> Siirto:
        siirto = input("Ensimmäisen pelaajan siirto: ")
        try:
            siirto = Siirto.from_str(siirto)
        except ValueError:
            print("Virheellinen siirto, yritä uudelleen.")
            return self._ensimmainen_siirto()
        return siirto

    def _toinen_siirto(self) -> Siirto:
        raise NotImplementedError


class KspPelaajaVsPelaaja(KiviSaksetPaperi):
    def _toinen_siirto(self) -> Siirto:
        siirto = input("Toisen pelaajan siirto: ")
        try:
            siirto = Siirto.from_str(siirto)
        except ValueError:
            print("Virheellinen siirto, yritä uudelleen.")
            return self._toinen_siirto()
        return siirto


class KspYksinkertainenTekoaly(KiviSaksetPaperi):
    def __init__(self):
        super().__init__()
        self.tekoaly = YksinkertainenTekoaly()

    def _toinen_siirto(self) -> Siirto:
        return self.tekoaly.anna_siirto()


class KspKehittynytTekoaly(KiviSaksetPaperi):
    def __init__(self):
        super().__init__()
        self.tekoaly = KehittynytTekoaly(10)

    def _toinen_siirto(self) -> Siirto:
        if self.tuomari.ekan_siirrot:
            self.tekoaly.lisaa_siirto(self.tuomari.ekan_siirrot[-1])
        siirto = self.tekoaly.anna_siirto()
        return siirto
