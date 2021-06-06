class Workshop():
    def Create_blade(self):
        pass

    def Create_handle(self):
        pass

    def Grind(self):
        pass

    def Finalize_weapon(self):
        pass


class One_Hand_Dagger(Workshop):
    def Create_blade(self):
        print("blade")

    def Create_handle(self):
        print("handle")

    def Grind(self):
        print("sharp blade")

    def Finalize_weapon(self):
        print("whole dagger done")


class BFS(Workshop):
    def Create_blade(self):
        print("blade")

    def Create_handle(self):
        print("handle")

    def Grind(self):
        print("sharp blade")

    def Finalize_weapon(self):
        print("whole sword done")


class Blcksmith():
    def __init__(self, workshop):
        self.workshop = workshop

    def Create_Weapon(self):
        self.workshop.Create_blade()
        self.workshop.Create_handle()
        self.workshop.Grind()
        self.workshop.Finalize_weapon()

if __name__ == "__main__":
    a = BFS()
    black = Blcksmith(a)
    black.Create_Weapon()
