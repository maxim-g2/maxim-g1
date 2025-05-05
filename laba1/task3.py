import random

def double():
    num = []
    for i in range(random.randint(5,10)):
        num.append(random.randint(1,20))
    print(num)
    print(len(num) != len(set(num)))

double()