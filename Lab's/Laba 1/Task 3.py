numbers = list(range(11))

num = int(input("Введите число от 0 до 9: "))


print(f"\nТаблица умножения для числа {num}:")
    
for i in numbers:
    print(f"{num} x {i} = {num * i}")
