class Player():
    def __init__(self,hp,attitude):
        self.hp = hp
        self.attitude = attitude
class State():
    def Cast_holy_shock(self,player):
        pass
class Enemy(State):
    def Cast_holy_shock(self,player):
        player.hp -= 10
class Ally(State):
    def Cast_holy_shock(self,player):
        player.hp += 20
class Holy_Shock():
    def __init__(self,state):
        self.state = state
    def Cast_holy_shock(self,player):
        self.state.Cast_holy_shock(player)
    def Check_state(self,player):
        if player.attitude == "Ally":
            self.state = Ally()
        if player.attitude == "Enemy":
            self.state = Enemy()
if __name__ == "__main__":
    player = Player(100,"Ally")
    spell = Holy_Shock(Enemy())
    spell.Check_state(player)
    spell.Cast_holy_shock(player)
    print(player.hp)