import random

def array():
    length = random.randint(1, 25)
    num = random.randint(3, 100) * 3


    arr = [num - 3 * i for i in range(length)]

    return arr

result = array()
print(f"Сгенерированный массив ({len(result)} элементов):")
print(result






