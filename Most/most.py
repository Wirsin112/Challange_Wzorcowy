class Enemy():
    def __init__(self, hp, speed, weapon):
        self.hp = hp
        self.speed = speed
        self.weapon = weapon

    def Swing(self):
        self.weapon.Swing()


class Ogre(Enemy):
    def __init__(self, hp, speed, weapon):
        super(Ogre, self).__init__(hp, speed, weapon)


class Troll(Enemy):
    def __init__(self, hp, speed, weapon):
        super(Troll, self).__init__(hp, speed, weapon)


class Weapon():
    def __init__(self, dmg, durability):
        self.dmg = dmg
        self.durability = durability

    def Swing(self):
        pass


class Mace(Weapon):
    def __init__(self, dmg, durability):
        super(Mace, self).__init__(dmg, durability)

    def Swing(self):
        print("Szusz")


class Axe(Weapon):
    def __init__(self, dmg, durability):
        super(Axe, self).__init__(dmg, durability)

    def Swing(self):
        print("Slash")


if __name__ == "__main__":
   w = Axe(50,100)
   o = Ogre(300,20,w)
   o.Swing()
