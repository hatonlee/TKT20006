from enum import Enum

class Siirto(Enum):
    KIVI = 1
    SAKSET = 2
    PAPERI = 3

    @classmethod
    def from_str(cls, siirto: str) -> Siirto:
        match siirto.lower():
            case "k":
                return cls.KIVI
            case "s":
                return cls.SAKSET
            case "p":
                return cls.PAPERI
            case _:
                raise ValueError("Virheellinen siirto")

    @classmethod
    def from_int(cls, siirto: int) -> Siirto:
        match siirto:
            case 1:
                return cls.KIVI
            case 2:
                return cls.SAKSET
            case 3:
                return cls.PAPERI
            case _:
                raise ValueError("Virheellinen siirto")
