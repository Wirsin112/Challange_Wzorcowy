class Dekoder():
    def Dekode(self,string):
        print(string)


class Cessar(Dekoder):
    def Dekode(self,string):
        print(string,"Tylko że po zastosowaniu cyfru cezara nie chciało mi się tego kodzić bo mam jeszcze kilka wzorców do napisania")

class Atbasz(Dekoder):
    def Dekode(self,string):
        print(string,"To samo co wyżej tylko po Atbasz")



if __name__ == "__main__":
    a = Atbasz()
    a.Dekode("Tajne haslo")