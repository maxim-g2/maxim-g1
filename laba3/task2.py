class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__rate = rate
        self.__surname = surname
        self.__days = days

    def get_salary(self):
        return self.__rate * self.__days

    def get_name(self):
        return self.__name

    def get_rate(self):
        return self.__rate

    def get_surname(self):
        return self.__surname

    def get_days(self):
        return self.__days


worker = Worker("Генерал", "Майонез", 10000, 3600)

print(f"Воркер {worker.get_name()} {worker.get_surname()} с заработной платой {worker.get_rate()} рублей проработал {worker.get_days()} дней")
print("И получил зарплату в размере", worker.get_salary(), "рублей")