from stringCalculator import Calculator

testValues = [
    ["1,2,5", 8],
    ["", 0],
    ["5,7,9", 21],
    ["0", 0],
    ["100, 101, 5", 206],
    ["1\n,2,3", 6],
    ["1,\n2,4", 7]
]

calculator = Calculator()

for pairs in testValues:
    total = calculator.add(pairs[0])
    if total == pairs[1]:
        print("Add succeeded for input: ", pairs[0], " result: ", str(total))
    else:
        print("Add should have equalled ", str(pairs[1]), " for input: ", pairs[0], "returned: ", total)
