from stringCalculator import Calculator

SyntaxErrorString= "SyntaxError"
testValues = [
    ["1,2,5", 8],
    ["", 0],
    ["5,7,9", 21],
    ["0", 0],
    ["100, 101, 5", 206],
    ["1\n,2,3", 6],
    ["1,\n2,4", 7],
    ["//;\n1;3;4", 8],
    ["//$\n1$2$3", 6],
    ["//@\n2@3@8", 13],
    ["//@@\n2@@5@@12", 19],
    ["-1,5", SyntaxErrorString],
    ["5,10,-12,-100", SyntaxErrorString],
    ["//%\n-5%6%12", SyntaxErrorString]
]

calculator = Calculator()

for pairs in testValues:
    try:
        total = calculator.add(pairs[0])
        if total == pairs[1]:
            print("Add succeeded for test: ", testValues.index(pairs), "result: ", total)
        else:
            print("Add should have equalled ", str(pairs[1]), " for test: ", testValues.index(pairs), "returned: ", total)
    except SyntaxError as value:
        if pairs[1] == "SyntaxError":
            print("Add succeeded for test: ", testValues.index(pairs), "result: SyntaxError - ", value)
        else:
            print("Add threw SyntaxError when it should not have for test: ", testValues.index(pairs))
