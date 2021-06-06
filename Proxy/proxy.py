class IShop():
    def Pay(self,money):
        pass

class Shop(IShop):
    def __init__(self,n):
        self.name = n
    def Pay(self,money):
        print("you bought something from",self.name,"for",money)

class Currency_Proxy(IShop):
    def __init__(self,shop):
        self.real = shop

    def Pay(self,money):
        if money == "zl":
            self.real.Pay(money)
        else:
            return "bad valet"

if __name__ == "__main__":
    a = Shop("boby")
    b = Currency_Proxy(a)
    b.Pay("zl")
