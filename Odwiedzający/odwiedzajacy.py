class Customer():
    def Visit_bakery(self, b):
        pass

    def Visit_butcher(self, b):
        pass


class Bob(Customer):
    def __init__(self, shop):
        self.shopping_list = shop

    def Visit_bakery(self, b):
        b.Accept_customer(self)

    def Visit_butcher(self, b):
        b.Accept_customer(self)


class Shop_Menager():
    def Accept_customer(self, customer):
        pass


class Beakery():
    def Accept_customer(self, customer):
        if "bread" in customer.shopping_list:
            self.Sell(customer)
        else:
            print("You don't have bread on your list so because covid you can't enter")

    def Sell(self, customer):
        customer.shopping_list.remove("bread")
        print("You bought bread")

class Butcher_shop():
    def Accept_customer(self, customer):
        if "meat" in customer.shopping_list:
            self.Sell(customer)
        else:
            print("You don't have meat on your list so because covid you can't enter")
    def Sell(self, customer):
        customer.shopping_list.remove("meat")
        print("You bought meat")
if __name__ == "__main__":
    b = Bob(["meat","boat"])
    beak = Beakery()
    meat = Butcher_shop()
    b.Visit_bakery(beak)
    b.Visit_butcher(meat)