from typing import Tuple
from tuomari import Tuomari
from tekoaly import YksinkertainenTekoaly, KehittynytTekoaly
from siirto import Siirto


class KiviSaksetPaperi:
    def __init__(self):
        self.tuomari = Tuomari()

    def pelaa_siirrot(self, ekan_siirto: Siirto, tokan_siirto: Siirto) -> str:
        """Kirjaa annetut siirrot ja palauttaa tuomarin tilan merkkijonona."""
        self.tuomari.kirjaa_piste(ekan_siirto, tokan_siirto)
        return str(self.tuomari)


class KspPelaajaVsPelaaja(KiviSaksetPaperi):
    """PvP - käytä `pelaa_siirrot` kutsua pelin ajamiseen."""
    pass


class KspYksinkertainenTekoaly(KiviSaksetPaperi):
    def __init__(self):
        super().__init__()
        self.tekoaly = YksinkertainenTekoaly()

    def pelaa_eka(self, ekan_siirto: Siirto) -> Tuple[Siirto, str]:
        """AI antaa tokan siirron; kirjaa pisteet ja palauttaa (toka_siirto, tuomari_str)."""
        toka = self.tekoaly.anna_siirto()
        self.tuomari.kirjaa_piste(ekan_siirto, toka)
        return toka, str(self.tuomari)


class KspKehittynytTekoaly(KiviSaksetPaperi):
    def __init__(self):
        super().__init__()
        self.tekoaly = KehittynytTekoaly(10)

    def pelaa_eka(self, ekan_siirto: Siirto) -> Tuple[Siirto, str]:
        if self.tuomari.ekan_siirrot:
            self.tekoaly.lisaa_siirto(self.tuomari.ekan_siirrot[-1])
        toka = self.tekoaly.anna_siirto()
        self.tuomari.kirjaa_piste(ekan_siirto, toka)
        return toka, str(self.tuomari)
