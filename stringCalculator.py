
class Calculator:

    @staticmethod
    def add(numbers):
        if not numbers:
            return 0
        else:
            values = list(map(int, numbers.split(",")))
            return sum(values)
