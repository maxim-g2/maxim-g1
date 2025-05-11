class Chest:
    def __init__(self, x=0 , y=0):
        self.__x = x
        self.__y = y

    def __del__(self):
        print(self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

chest = Chest()
print(chest.x,  chest.y)

chest.x = 52
print(chest.x,  chest.y)

chest.y = 42
print(chest.x,  chest.y)
