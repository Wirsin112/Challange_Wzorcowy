import random
class Stage():
    def __init__(self,enemys):
        self.enemys = enemys
    def Start(self):
        for i in range(5):
            self.Spawn_enemy()

    def Spawn_enemy(self):
        r = random.randint(0,1)
        print(r)
        return self.enemys[r].Clone()

class Enemy():
    def __init__(self,name,hp,dmg,speed):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.speed = speed

    def Clone(self):
        a = Enemy(self.name,self.hp,self.dmg,self.speed)
        return a

class Dragon(Enemy):
    def __init__(self, name, hp, dmg, speed,fly):
        super(Dragon,self).__init__(name,hp,dmg,speed)
        self.fly = fly

    def Clone(self):
        a = Dragon(self.name, self.hp, self.dmg, self.speed,self.fly)
        return a


class Troll(Enemy):
    def __init__(self, name, hp, dmg, speed, stun):
        super(Troll, self).__init__(name, hp, dmg, speed)
        self.stun = stun

    def Clone(self):
        a = Dragon(self.name, self.hp, self.dmg, self.speed, self.stun)
        return a

if __name__== "__main__":
    d = Dragon("dragon",800,100,30,5)
    t = Troll("troll", 100, 20, 5, 1)
    s = Stage([d,t])
    s.Start()