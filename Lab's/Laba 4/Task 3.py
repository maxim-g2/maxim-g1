from enum import Enum

class MathOperation(Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

def calculate(a, b, operation: MathOperation):

    match operation:
        case MathOperation.ADD:
            result = a + b
        case MathOperation.SUBTRACT:
            result = a - b
        case MathOperation.MULTIPLY:
            result = a * b
        case MathOperation.DIVIDE:
            result = a / b if b != 0 else float('inf')

    return (a, b, operation.value, result)

print(calculate(5, 3, MathOperation.ADD))
print(calculate(10, 2, MathOperation.DIVIDE))
