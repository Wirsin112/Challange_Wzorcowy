class Czlowiek():
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def wykop_suroweic(self, surowiec):
        print("wykopalem", surowiec.nazwa)

    def uszkodz_powloke_ozonowa(self, ziemia):
        z = ziemia.zwroc()
        z.powloka -= 0.001
        print(z.powloka)


class Surowiec():
    def __init__(self, nazwa, ilosc):
        self.nazwa = nazwa
        self.ilosc = ilosc


class Ziemia():
    def _init_(self, ludzie, surowce, powloka):
        self.powloka = powloka
        self.ludzie = ludzie
        self.surowce = surowce

    def zwroc(self):
        return self


if __name__ == "__main__":
    c = Czlowiek("jan", "wan")
    s = Surowiec("wegiel", 500)
    Z = Ziemia()
    Z._init_([c], [s], 1.0)
    c.wykop_suroweic(s)
    c.uszkodz_powloke_ozonowa(Z)