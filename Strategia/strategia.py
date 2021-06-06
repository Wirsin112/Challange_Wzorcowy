class Deus_Ex():
    def __init__(self, play_style):
        self.play_style = play_style

    def kill(self):
        self.play_style.kill()


class Play_Style():
    def kill(self):
        pass


class Stelth(Play_Style):
    def kill(self):
        print("silence")


class Loud(Play_Style):
    def kill(self):
        print("loud")


if __name__ == "__main__":
    s = Stelth()
    de = Deus_Ex(s)
    de.kill()
