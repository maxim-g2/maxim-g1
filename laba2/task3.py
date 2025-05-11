class chest:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def max(self):
        return self.x if self.x > self.y else self.y

chests = chest(42,52)

print(f"Максимальное число {chests.max()}, сумма чисел {chests.sum()}")

chests.set_x(14)
print(f"Максимальное число {chests.max()}, сумма чисел {chests.sum()}")

chests.set_y(22)
print(f"Максимальное число {chests.max()}, сумма чисел {chests.sum()}")