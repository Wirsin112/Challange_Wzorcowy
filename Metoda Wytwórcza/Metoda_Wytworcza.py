import random
class Czar():
    def __init__(self,mana,type,nazwa):
        self.mana = mana
        self.typ = type
        self.nazwa = nazwa
class Kula_Ognia(Czar):
    def __init__(self,koszt):
        super().__init__(10,"ognisty","Kula,Ognia")
class Kula_Ognia(Czar):
    def __init__(self,koszt):
        self.koszt_many = koszt
        super().__init__(True,"ogien","Kula_Ognia")


class Tornado(Czar):
    def __init__(self,koszt):
        self.koszt_many = koszt
        super().__init__(True,"powietrze","Tornado")


class Aura_Miecza(Czar):
    def __init__(self,koszt):
        self.koszt_energi = koszt
        super().__init__(False,"aura","Aura_Miecza")

class Gracz():
    def __init__(self,hp,mp,nazwa):
        self.zycie = hp
        self.mana = mp
        self.nazwa = nazwa
        self.energia = 5
        self.czary = [Kula_Ognia,Tornado,Aura_Miecza]
    def Uzyj_czaru(self):
        a = random.randint(0,len(self.czary)-1)
        czar = self.czary[a](5)
        print("Uzyles czaru",czar.nazwa)
        return czar

if __name__ == "__main__":
    gracz = Gracz(100,20,"Bob")
    gracz.Uzyj_czaru()
