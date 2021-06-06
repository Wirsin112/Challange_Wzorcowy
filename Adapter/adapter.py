class Messenge():
    def __init__(self,string):
        self.text = string
class Human():
    def Text(self,string,elf):
        a = Messenge(string)
        elf.mes_list.append(a)

class Translator():
    def Translate_Human_Elf(self,m):
        #do some fancy stuff to translate for example i have simple if
        if m.text == "hi":
            print("Eluwina")
        else:
            print("teach me this word first")

class Elf():
    def __init__(self):
        self.mes_list = []
        self.translator = Translator()

    def Read(self):
        if len(self.mes_list) != 0:
            self.translator.Translate_Human_Elf(self.mes_list[0])

if __name__ == "__main__":
    Elf = Elf()
    h = Human()
    h.Text("hi",Elf)
    Elf.Read()



