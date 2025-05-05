class Train:
    def __init__(self,destination, train_num, departure_time):
        self.destination = destination
        self.train_num = train_num
        self.departure_time = departure_time

    def get_info(self):
        return((f"Название пункта назначения:  {self.destination}\n"
              f"Номер поезда: {self.train_num}\n"
              f"Время выезда: {self.departure_time}\n"))

    def search_train(self):
            search_train_departure_time = input("Введите время выезда в формате 00:00")
            search_train_destination = input("Введите пункт назначения")
            if search_train_departure_time == Trains.departure_time and search_train_destination == Trains.destination:
                print(f"Такой поезд есть\n {Trains.get_info()}")
            else:
                print("Такого поезда нету")

    def change_departure_time(self, new_departure_time):
        self.departure_time = new_departure_time

    def change_destination(self, new_destination):
        self.destination = new_destination

    def change_train_num(self, new_train_num):
        self.train_num = new_train_num

Trains = Train("Владивосток", "555", "20:00")


while True:
    i = int(input(("Выберите что хотите сделать:\n"
      "1 - Вывести информацию о поезде\n"
      "2 - Изменить пункт назначения поезда\n"
      "3 - Изменить время отбытия\n"
      "4 - Изменить номер поезда\n"
      "5 - Поиск поезда\n"
      "6 - Выход\n")))
    if i == 1:
        print(Trains.get_info())
    if i == 2:
        Trains.change_destination(input("Введите новый пункт назначения: "))
        print(f"Новый пункт назначения: {Trains.destination}")
    if i == 3:
        Trains.change_departure_time(input("Введите новое время отбытия: "))
        print(f"Новое время отбытия: {Trains.departure_time}")
    if i == 4:
        Trains.change_train_num(input("Введите новый номер поезда: "))
        print(f"Новый номер позеда: {Trains.train_num}")
    if i == 5:
        Trains.search_train()
    if i == 6:
        break