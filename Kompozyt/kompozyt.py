class Enemys():
    def Attack(self):
        pass
    def Move(self):
        pass

class Ogre(Enemys):
    def __init__(self,hp,dmg,speed):
        self.hp = hp
        self.dmg = dmg
        self.speed = speed
    def Attack(self):
        print(str(self.dmg))
    def Move(self):
        print(str(self.Move()))

class Composite(Enemys):
    def __init__(self,enemys):
        self.enemys = enemys

    def Attack(self):
        for i in self.enemys:
            print(str(i.dmg))
    def Move(self):
        for i in self.enemys:
            print(str(i.speed))

if __name__ == "__main__":
    a = Ogre(100,20,30)
    a1 = Ogre(100, 12, 20)
    a2 = Ogre(100, 41, 20)
    a3 = Ogre(100, 1, 30)
    a4 = Ogre(100, 3, 30)
    com = Composite([a,a1,a2,a3,a4])
    com.Attack()
    com.Move()