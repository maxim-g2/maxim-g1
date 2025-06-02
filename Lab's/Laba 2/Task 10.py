elements = []

while True:
    a = input("Введите элемент (пустая строка для завершения): ")
    if a == "":
        break
    elements.append(a)

if elements:
    shortest = min(elements, key=len)
    longest = max(elements, key=len)

    print(f"Самый короткий элемент: '{shortest}'")
    print(f"Самый длинный элемент: '{longest}'")
else:
    print("Список пуст")