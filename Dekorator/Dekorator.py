class IMistyczny_Guizk():
    def Wcisnij_przycisk(self):
        print('Wcisnąłem guzik')


class Mistyczny_Guzik(IMistyczny_Guizk):
    def Wcisnij_przycisk(self):
        print('Tak')


class Dekorator():
    def __init__(self,IM):
        self.guzik = IM

    def Wcisnij_przycisk(self):
        pass


class Swiatlo(Dekorator):
    def __init__(self, IM):
        self.guzik = IM

    def Wcisnij_przycisk(self):
        self.guzik.Wcisnij_przycisk()
        print("Swiatlo zapalone")

class Hiroshima(Dekorator):
    def __init__(self, IM):
        self.guzik = IM

    def Wcisnij_przycisk(self):
        self.guzik.Wcisnij_przycisk()
        print("Wystartowales 3 wojne swiatowa i zmarnowales dobra atomowke")

class Komputer(Dekorator):
    def __init__(self, IM):
        self.guzik = IM

    def Wcisnij_przycisk(self):
        print("Shhhhh! Wlaczony")
class Click(Dekorator):
    def __init__(self, IM):
        self.guzik = IM

    def Wcisnij_przycisk(self):
        self.guzik.Wcisnij_przycisk()
        print("Click")


if __name__ == "__main__":
    im = IMistyczny_Guizk()
    dek = Dekorator(im)
    a = Swiatlo(im)
    a.Wcisnij_przycisk()

