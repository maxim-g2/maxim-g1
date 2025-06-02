def numbers(nums):

    count = 0
    for num in nums:
        if num > 0:
            count += 1
    return count

print(numbers([1, -2, 3, 0, 4.5]))
