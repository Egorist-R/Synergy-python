class Kassa:
    def __init__(self, money):
        self.money = money

    def top_up(self, X):
        self.money = self.money + X

    def count_1000(self):
        thousands = self.money // 1000
        print(thousands)
        return thousands

    def take_away(self, X):
        if X > self.money:
            raise ValueError("В кассе не достаточно денег")
        else:
            self.money = self.money - X

my_cash = Kassa(4500)

my_cash.count_1000()

my_cash.top_up(1200)

my_cash.count_1000()

my_cash.take_away(3000)

my_cash.count_1000()
