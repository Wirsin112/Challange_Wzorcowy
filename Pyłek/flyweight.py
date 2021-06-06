class Model():
    def __init__(self, path):
        self.path = path


class Ogre():
    def __init__(self, model):
        self.model = model


class Ogre_Wizzard(Ogre):
    def __init__(self,a):
        super(Ogre_Wizzard,self).__init__(a)


class Ogre_Axeman(Ogre):
    def __init__(self, a):
        super(Ogre_Axeman,self).__init__(a)


if __name__ == "__main__":
    m = Model("/skin.jpg")
    o = Ogre_Wizzard(m)
    print(o.model.path)
