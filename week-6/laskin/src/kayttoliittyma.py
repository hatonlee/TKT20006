from enum import Enum
from tkinter import ttk, constants, StringVar


class Summa:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
        self._kumoa = 0

    def suorita(self):
        luku = int(self.io() or 0)
        self._kumoa = luku
        self.sovelluslogiikka.plus(luku)

    def kumoa(self):
        self.sovelluslogiikka.miinus(self._kumoa)


class Erotus:
    def __init__(self, sovelluslogiikka, io):
        self.sovelluslogiikka = sovelluslogiikka
        self.io = io
        self._kumoa = 0

    def suorita(self):
        luku = int(self.io() or 0)
        self._kumoa = luku
        self.sovelluslogiikka.miinus(luku)

    def kumoa(self):
        self.sovelluslogiikka.plus(self._kumoa)


class Nollaus:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._kumoa = 0

    def suorita(self):
        self._kumoa = self._sovelluslogiikka.arvo()
        self._sovelluslogiikka.nollaa()

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._kumoa)


class Kumoa:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_operaatio = None

    def suorita(self):
        print(self._edellinen_operaatio)
        self._edellinen_operaatio.kumoa()


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
            Komento.KUMOA: Kumoa(sovelluslogiikka)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        print(komento_olio)
        komento_olio.suorita()
        self._komennot[Komento.KUMOA]._edellinen_operaatio = komento_olio
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
