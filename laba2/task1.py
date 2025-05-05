class Student:
    def __init__(self,surname,birthday,group_number,grade):
        self.surname = surname
        self.birthday = birthday
        self.group_number = group_number
        self.grade = grade

    def get_info(self):
        return((f"Фамилия:  {self.surname}\n"
              f"Дата рождения: {self.birthday}\n"
              f"Номер группы: {self.group_number}\n"
              f"Успеваемость: {self.grade}\n"))

    def search_student(self):
            search_student_surname = input("Введите Фамилию")
            search_student_birthday = input("Введите дату рождения студента в формате день.месяц.год")
            if search_student_surname == Students.surname and search_student_birthday == Students.birthday:
                print(f"Такой студент есть\n {Students.get_info()}")
            else:
                print("Такого студента нету")

    def change_surname(self, new_surname):
        self.surname = new_surname

    def change_birthday(self, new_birthday):
        self.birthday = new_birthday

    def change_group_number(self, new_group_number):
        self.group_number = new_group_number

Students = Student("Петров", "13.04.2004", "153", ["5","5","5","5","5"])

while True:
    i = int(input(("Выберите что хотите сделать:\n"
      "1 - Вывести информацию о студенте\n"
      "2 - Изменить фамимлию\n"
      "3 - Изменить дату рождения\n"
      "4 - Изменить номер группы\n"
      "5 - Поиск студента\n"
      "6 - Выход\n")))
    if i == 1:
        print(Students.get_info())
    if i == 2:
        Students.change_surname(input("Введите новую фамилию студента: "))
        print(f"Новая фамилия: {Students.surname}")
    if i == 3:
        Students.change_birthday(input("Введите новую дату рождения: "))
        print(f"Новая дата рождения: {Students.birthday}")
    if i == 4:
        Students.change_group_number(input("Введите новый номер группы: "))
        print(f"Новая группа студента: {Students.group_number}")
    if i == 5:
        Students.search_student()
    if i == 6:
        break


