import random
class Player_menager():
    def __init__(self, comand, player):
        self.comands = comand
        self.player = player

    def Do(self):
        r = random.randint(0,1)
        self.comands[r].Do(self.player)


class Command():
    def Do(self, player):
        pass


class Move(Command):
    def Do(self, player):
        player.x += 1


class Climb(Command):
    def Do(self, player):
        player.y += 1


class Player():
    def __init__(self):
        self.x = 0
        self.y = 0


if __name__ == "__main__":
    a = Move()
    b = Climb()
    player = Player()
    player_m = Player_menager([a,b],player)
    player_m.Do()
    print(str(player_m.player.x),str(player_m.player.y))
