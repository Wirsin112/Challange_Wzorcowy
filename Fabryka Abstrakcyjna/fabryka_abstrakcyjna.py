class Player():
    def __init__(self, factory):
        self.factorys = factory
        self.sword = None
        self.shield = None

    def Create_stuff(self, f):
        self.shield = f.Create_shield()
        self.sword = f.Create_sword()


class Crafting():
    def Create_shield(self):
        pass

    def Create_sword(self):
        pass


class Tier1_Factory(Crafting):
    def Create_shield(self):
        return T1_Shield()

    def Create_sword(self):
        return T1_Sword()


class Tier2_Factory(Crafting):
    def Create_shield(self):
        return T2_Shield()

    def Create_sword(self):
        return T2_Sword()


class Shield():
    pass


class Sword():
    pass


class T1_Sword(Sword):
    pass


class T2_Sword(Sword):
    pass


class T1_Shield(Sword):
    pass


class T2_Shield(Sword):
    pass

if __name__ == "__main__":
    t1 = Tier1_Factory()
    t2 = Tier2_Factory()
    p = Player([t1,t2])
    p.Create_stuff(p.factorys[1])
    print(p.shield,p.sword)