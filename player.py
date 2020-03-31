import prices
class Player:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.owns = {
            "money":    10,
            "sur1":     0,
            "sur2":     35,
            "points":   1,
#            "fab1":     True,
#            "fab2":     False
        }
        self.toBuy = {
            "sur1":     2,
            "sur2":     0,
#            "fab1":     False,
#            "fab2":     True
        }
        self.toSell = {
            "sur1":     0,
            "sur2":     10,
        }

    def buy(self):
        for x in self.toBuy: 
            price = prices.get(x)
            newmoney = self.owns["money"] - price * self.toBuy[x]
            if (newmoney >= 0):
                self.owns["money"] = newmoney
                self.owns[x] += self.toBuy[x]
            else:
                print("Cannot buy %s, not enough money" % x)
            self.toBuy[x] = 0


    def sell(self):
        for x in self.toSell:
            price = prices.get(x)
            newamount = self.owns[x] - self.toSell[x]
            if (newamount >=0):
                self.owns["money"] += price * self.toSell[x]
                self.owns[x] = newamount
            else:
                print("Cannot sell %s, not enough resources" % x)
            self.toSell[x] = 0
