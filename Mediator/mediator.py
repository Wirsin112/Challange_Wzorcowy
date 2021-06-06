class Mediator():
    def __init__(self):
        self.players = []

    def notify(self, player):
        for i in (self.players):
            if i is not player:
                print(i.nick, "you have new offer from", player.nick)


class Player():
    def __init__(self, nick):
        self.nick = nick

    def Get_mediator(self, mediator):
        self.mediator = mediator
        self.mediator.players.append(self)

    def Make_an_offer(self):
        self.mediator.notify(self)


if __name__ == "__main__":
    p = Player("bob")
    p1 = Player("pop")
    p2 = Player("abc")
    m = Mediator()
    p.Get_mediator(m)
    p1.Get_mediator(m)
    p2.Get_mediator(m)
    p.Make_an_offer()
