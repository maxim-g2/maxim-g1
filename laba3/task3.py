class Calculation:
    def __init__(self):
        self.calculation_line = ""

    def set_calculation_line(self, calculation_line: str):
        self.calculation_line = calculation_line

    def delete_last_symbol(self):
        self.calculation_line = self.calculation_line[:-1]

    def get_calculation_line(self):
        return self.calculation_line

    def set_last_symbol_calculation_line(self, char: str):
        if len(char) != 1:
            raise ValueError("Принимается один символ")

        self.calculation_line += char

    def get_last_symbol(self):
        if len(self.calculation_line) == 0:
            return ""
        return self.calculation_line[-1]

calculation = Calculation()

calculation.set_calculation_line("2 + 2")
print(f"Строка: {calculation.get_calculation_line()}")

calculation.set_last_symbol_calculation_line("*")
print(f"Строка с добавленным символом: {calculation.get_calculation_line()}")

last_char = calculation.get_last_symbol()
print(f"Последний символ: {last_char}")

calculation.delete_last_symbol()
print(f"Строка после удаления: {calculation.get_calculation_line()}")