
# String Calculator
- Takes string numbers and returns the result as int after calculation.

## Instructions
- We can add two numbers by passing a string to the `Add` function
    - Examples below:
        - string_calculator.Add('2,3,4')
        - string_calculator.Add('2\n3\n4')
- We can add custom delimeters by using `//[<delimeter>]\n<operand><delimeter><operand>`
- Ensure you add the new line and also operands should be separated by delimeter
- We can also add multiple delimeters using `//[<delimeter>][<delimeter2>]\n<operand><delimeter><operand><delimeter2><operand>`

## Assumptions
- I am assuming that the headers are always valid for multi delimeter tests.
- New lines will not be used as a custom delimeter
- default delimeters are `,` and `\n` so they run without the custom delimeter syntax.