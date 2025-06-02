import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 10))

print("Сгенерированная коллекция:", numbers)


min_number = min(numbers)
print("Минимальный элемент коллекции:", min_number)