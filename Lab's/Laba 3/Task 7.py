def decreasing(number):

    digits = [int(d) for d in str(number)]
    for i in range(len(digits) - 1):
        if digits[i] <= digits[i+1]:
            return False
    return True

print(decreasing(54321))
print(decreasing(44321))



