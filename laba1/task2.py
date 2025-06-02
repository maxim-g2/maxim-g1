def combination_sum2(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, path, target):
        if target == 0:
            result.append(list(path))
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, target - candidates[i])
            path.pop()
    backtrack(0, [], target)
    return result
candidates = list(map(int, input("Введите список кандидатов через пробел: ").split()))
target = int(input("Введите целевую сумму: "))
print(combination_sum2(candidates, target))