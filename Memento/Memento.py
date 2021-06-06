class Player():
    def __init__(self, name):
        self.name = name


class Memento():
    def __init__(self, p1, p2, moves):
        self.player1 = p1
        self.player2 = p2
        self.moves = moves


class Chess_Game():
    def __init__(self, p1, p2, moves):
        self.player1 = p1
        self.player2 = p2
        self.moves = moves
        self.games = []

    def Save_match(self):
        a = Memento(self.player1, self.player2, self.moves)
        self.games.append(a)

    def Remind_game(self, memento):
        self.player1 = memento.player1
        self.player2 = memento.player2
        self.moves = memento.moves

if __name__ == "__main__":
    a = Chess_Game("Fisher", "Rudecki",["e4","e5","Nf6"])
    a.Save_match()

