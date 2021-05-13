class Observer():
    def update(self,wiadomosc):
        print("Nowa wiadomosc")

class Klient(Observer):
    def __init__(self, name):
        self.name = name
    def update(self,wiadomsc):
        print(wiadomsc)

class Sklep():
    def __init__(self,klienci,produkty):
        self.kilenic = klienci
        self.pordukty = produkty
    def powiadom(self,wiad):
        for i in self.kilenic:
            i.update(wiad)
    def dodaj_klienta(self,kilent):
        self.kilenic.append(kilent)
    def usun_klienta(self,klient):
        self.kilenic.remove(klient)
    def dodaj_produkt(self,nazwa):
        self.pordukty.append(nazwa)
        self.powiadom("nazwa")

if __name__ == "__main__":
    a = Klient("piesek")
    b = Klient("pies")
    sklep =Sklep([a,b],["buty","spodnie"])
    sklep.powiadom("buty")
    sklep.dodaj_produkt("czapki")
    sklep.usun_klienta(a)
    sklep.powiadom("witam")