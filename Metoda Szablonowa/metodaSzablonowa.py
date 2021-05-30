import random


class Wizard():
    def __init__(self, hp, aspect):
        self.hp = hp
        self.aspect = aspect

    def Move(self):
        rand = random.randint(0, 3)
        if rand == 0:
            print(chr(0x2B60))
        if rand == 1:
            print(chr(0x2B61))
        if rand == 2:
            print(chr(0x2B62))
        if rand == 3:
            print(chr(0x2B63))

    def Rest(self):
        self.hp += 10

    def Cast_main_spell(self):
        pass


class Fire_Wizard(Wizard):
    def __init__(self, hp, aspect):
        Wizard.__init__(self,hp, aspect)

    def Cast_main_spell(self):
        print("Skwierczenie plomeni")


class Frost_Wizard(Wizard):
    def __init__(self, hp, aspect):
        Wizard.__init__(self,hp, aspect)

    def Cast_main_spell(self):
        print("Dzwiek pekajacego lodu")


if __name__ == "__main__":
    w = Frost_Wizard(100, "Red")
    w.Move()
    w.Cast_main_spell()
