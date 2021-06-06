class Iterator():
    def Next(self):
        pass

    def End(self):
        pass


class SimpleIterator(Iterator):
    def __init__(self, pack):
        self.pack = pack
        self.mob_number = 0

    def Next(self):
        if self.End() == False:
            if self.pack.mob_pack[self.mob_number].Is_alive() == False:
                self.pack.mob_pack.remove(self.pack.mob_pack[self.mob_number])
            else:
                print(self.pack.mob_pack[self.mob_number].hp)
                self.mob_number += 1;
            self.Next()

    def End(self):
        if self.mob_number == len(self.pack.mob_pack):
            return True
        else:
            return False


class Iterable():
    def Get_Iterator(self):
        pass


class Mobs_Pack():
    def __init__(self):
        self.mob_pack = []

    def Get_Iterator(self):
        self.iterator = SimpleIterator(self)

    def Add_mob(self, mob):
        self.mob_pack.append(mob)


class Mob():
    def __init__(self, hp):
        self.hp = hp

    def Is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

if __name__ == "__main__":
    a = Mobs_Pack()
    a.Add_mob(Mob(30))
    a.Add_mob(Mob(3))
    a.Add_mob(Mob(-3))
    a.Add_mob(Mob(0))
    a.Add_mob(Mob(100))
    a.Add_mob(Mob(0))
    a.Get_Iterator()
    a.iterator.Next()
    print(a.iterator.pack.mob_pack)
