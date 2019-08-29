
class Calculator:

    @staticmethod
    def add(numbers):
        if not numbers:
            return 0
        else:
            numbers = numbers.replace('\n', '')
            values = list(map(int, numbers.split(',')))
            return sum(values)
