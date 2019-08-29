# StringCalculator

StringCalculator includes a Calculator class that can be used to add numbers contained in a string formatted using a custom delimiter format.
Delimiter format is such that the string should contain:
“//[delimiter]\n[delimiter separated numbers]”
As an example, "//@\n5@5" will result in 10 being returned.
If no delimiter is given, ',' is assumed to be the delimiter.

Note: Negative values will result in a ValueError
Note: Values greater than 1000 will be ignored
Note: Delimiters can be any value in length, but only one delimter is supported.

testcalculator includes a short list of test strings, including the expected outcome. In the case where a negative number is given, the test expects a SyntaxError to be raised.

testCalculator can be run by:

python testCalculator
