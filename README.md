
# String Calculator
- Takes string numbers and returns the result as int after calculation.

## Instructions
- We can add two numbers by passing a string to the `Add` function
    - Examples below:
        - `string_calculator.Add('2,3,4')`
        - `string_calculator.Add('2\n3\n4')`
- We can add custom delimeters by using `//[<delimeter>]\n<operand><delimeter><operand>`
- Ensure you add the new line and also operands should be separated by delimeter
    - Examples below:
        - `string_calculator.Add('//[,]\n2,3,4')`
        - `string_calculator.Add('//[||]\n2||3||4')`
- We can also add multiple delimeters using `//[<delimeter>][<delimeter2>]\n<operand><delimeter><operand><delimeter2><operand>`
    - Examples below:
        - `string_calculator.Add('//[,][|]\n2,3|4')`
        - `string_calculator.Add('//[||][**]\n2**3||4')`

## Assumptions
- I am assuming that the headers are always valid for multi delimeter tests.
- New lines will not be used as a custom delimeter
- default delimeters are `,` and `\n` so they run without the custom delimeter syntax.
- Coverage is tested and at 100% so no tests were added for `_to_number` function