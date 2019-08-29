class Calculator:

    @staticmethod
    def add(numbers):
        if not numbers:
            return 0
        else:
            delimiter = ','
            if numbers[0:2] == "//":
                split_numbers = numbers.split('\n', 1)
                delimiter = split_numbers[0][2:]
                numbers = split_numbers[1]
            numbers = numbers.replace('\n', '')
            values = list(map(int, numbers.split(delimiter)))
            negatives = [i for i in values if i < 0]
            if negatives:
                raise SyntaxError("Negatives not allowed: " + str(negatives))
            values_within_limit = [i for i in values if 1000 > i > 0]
            return sum(values_within_limit)
