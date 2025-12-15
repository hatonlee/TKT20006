from ksp import KspPelaajaVsPelaaja, KspYksinkertainenTekoaly, KspKehittynytTekoaly
import sys
import os

class Cli:
    @staticmethod
    def tulosta_ohjeet():
        print(
            "Valitse pelimuoto:"
            "\n (a) PvP"
            "\n (b) Yksinkertainen tekoäly"
            "\n (c) Kehittynyt tekoäly"
            "\n (q) Lopeta"
        )

    @staticmethod
    def tyhjenna_ruutu():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def valitse_peli():
        valinta = input().lower()
        match valinta:
            case "a":
                return KspPelaajaVsPelaaja()
            case "b":
                return KspYksinkertainenTekoaly()
            case "c":
                return KspKehittynytTekoaly()
            case "q":
                sys.exit()
            case _:
                print("Virheellinen valinta, yritä uudelleen.")
                return Cli.valitse_peli()


def main():
    Cli.tulosta_ohjeet()
    peli = Cli.valitse_peli()
    Cli.tyhjenna_ruutu()
    while True:
        peli.pelaa()


if __name__ == "__main__":
    main()
