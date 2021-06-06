import random


class Case():
    def Roll(self):
        pass

class Six(Case):
    def Roll(self):
        print("6")

class Not_Six(Case):
    def Roll(self):
        print("not 6")

class Dice_Roll():
    def __init__(self,number):
        self.dices = []
        self.number = number
    def Roll_them(self):
        for i in range(self.number):
            roll = random.randint(1,6)
            if roll == 6:
                self.dices.append(Six())
            else:
                self.dices.append(Not_Six())
    def Add_dice(self):
        self.number += 1

    def Remove_dice(self):
        if self.number > 0:
            self.number -= 1

if __name__ == "__main__":
    a = Dice_Roll(5)
    a.Roll_them()
    print(a.dices)