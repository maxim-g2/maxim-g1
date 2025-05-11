class Count:
    def __init__(self, count_value=0):
        self.__count = count_value

    def decrease(self):
        self.__count -= 1

    def increase(self):
        self.__count += 1

    @property
    def count(self):
        return self.__count


lvl_count = Count(3)
print("Уровень: ", lvl_count.count)

lvl_count.increase()
print("Уровень: ", lvl_count.count)

lvl_count.decrease()
print("Уровень: ", lvl_count.count)


