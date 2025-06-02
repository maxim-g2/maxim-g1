def num(numbers):

    num = 1
    for i in range(len(numbers)):
        if (i + 1) % 2 != 0:
            num *= numbers[i]
    return num

print(num([1, 2, 3, 4, 5]))


