class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.rate = rate
        self.surname = surname
        self.days = days

    def get_salary(self):
        return self.rate * self.days


worker = Worker("Генерал", "Майонез", 10000, 3600)

print(f"Воркер {worker.name} {worker.surname} с заработной платой {worker.rate} рублей проработал {worker.days} дней")
print("И получил зарплату в размере", worker.get_salary(), "рублей")