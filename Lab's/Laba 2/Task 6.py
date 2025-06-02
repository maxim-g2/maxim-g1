def divisor(a: int, b: int) -> bool:

    if a == 0:
        return False
    return b % a == 0

print(divisor(2, 10))
print(divisor(0, 5))