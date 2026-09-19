class Cherepashka:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y 
        self.s = s

    def go_up(self):
        self.y = self.y + self.s

    def go_down(self):
        self.y = self.y - self.s

    def go_left(self):
        self.x = self.x - self.s

    def go_right(self):
        self.x = self.x + self.s

    def evolve(self):
        self.s = self.s + 1

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Ошибка: шаг s не может быть меньше или равен 0!")
        self.s = self.s - 1

    def count_moves(self, x2, y2):
        distance_x = abs(x2 - self.x)
        distance_y = abs(y2 - self.y)

        moves_x = distance_x // self.s
        if distance_x % self.s != 0:
            moves_x = moves_x + 1

        moves_y = distance_y // self.s
        if distance_y % self.s != 0:
            moves_y = moves_y + 1

        return moves_x + moves_y

turt = Cherepashka(0, 0, 2)

turt.go_up()
turt.go_right()

print(f"Сейчас черепашка в точке: ({turt.x}, {turt.y})")
print("Минимум шагов до (5,5):", turt.count_moves(5, 5))
