import time


class Piec():
    def __init__(self, czas):
        self.czas = czas

    def piecz(self):
        time.sleep(self.czas)
        print("upieczone")


class Maszyna_do_skladnikow():
    def __init__(self, receptura):
        self.receptura = receptura

    def Mieszaj(self):
        for i in self.receptura:
            print("Dodaj", i)
        for i in range(5):
            print("mieszam")
        print("ciasto gotowe")


class Maszyna_do_pakowania():
    def __init__(self, folia):
        self.folia = folia

    def Opakuj(self):
        if self.folia - 5 > 0:
            print("opakowano")
            self.folia -= 5
            return False
        else:
            print("dodaj folie")
            return True

    def Uzupelnij_Folie(self, folia):
        self.folia += folia
        print("Folia uzupelniona")


class System_kontoli():
    def __init__(self, partia, m1, m2, m3):
        self.partia = partia
        self.Maszyna_skladniki = m1
        self.Piec = m2
        self.Maszyna_pakownie = m3

    def Uruchom(self):
        for i in range(self.partia):
            self.Maszyna_skladniki.Mieszaj()
            self.Piec.piecz()
            if self.Maszyna_pakownie.Opakuj():
                self.Maszyna_pakownie.Uzupelnij_Folie(30)


class User():
    def __init__(self, system):
        self.system = system

    def Zrob_Paluszki(self):
        self.system.Uruchom()


if __name__ == "__main__":
    piec = Piec(1)
    m1 = Maszyna_do_pakowania(7)
    m2 = Maszyna_do_skladnikow(["jajka", "maka", "leko", "sol", "sezam", "pokurszone dusze biednych studentow"])
    System = System_kontoli(5, m2, piec,m1)
    User = User(System)
    User.Zrob_Paluszki()
