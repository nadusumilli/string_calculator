import re
from exceptions import InvalidValueException, NegativeNumberException


class StringCalculator:
    """
        String Calculator, performs mathematical calculations on strings.
    """

    def __init__(self):
        self.delimeter = ",|\n"
        self.call_count = 0

    def GetCalledCount(self):
        return self.call_count

    def _to_number(self, operands):
        result = []
        self.call_count += 1
        try:
            if operands.startswith("//"):
                # Get the header with delimeter and numbers separately.
                header, numbers = operands.split("\n")

                # This regex finds all delimiters enclosed in square brackets,
                # including multi-character delimiters.
                delimeters = re.findall(r"\[(.*?)\]", header)

                # Adding the default delimeters.
                delimeters.extend(self.delimeter.split("|"))

                # Ensure that the delimeters for splitting are added with a regex.
                # The regex is in the form of `<delimeter>|<delimeter>`.
                self.delimeter = "|".join(map(re.escape, delimeters))

                # Split the the string with regex and get all operands
                operands = re.split(self.delimeter, numbers)

                # remove numbers greater than 1000
                operands = [x for x in operands if int(x) <= 1000]

                # validate the numbers
                negativeNumbers = [x for x in operands if int(x) < 0]
                if len(negativeNumbers) > 0:
                    raise NegativeNumberException(
                        f"negatives not allowed: {",".join(negativeNumbers)}")
            else:
                # If there is no delimeter in the string, pull defaults and apply.
                self.delimeter = "|".join(map(re.escape, self.delimeter))
                operands = re.split(self.delimeter, operands)

            # Perform the conversions and return the numbers list.
            if isinstance(operands, list) and len(operands) > 1:
                result.extend([float(x) if "." in x else int(x)
                              for x in operands])
            else:
                result.append(float(operands[0])
                              if "." in operands[0] else int(operands[0]))

            # return the result numbers list.
            return result
        except ValueError:
            # If there is an error return the custom error message.
            raise InvalidValueException(
                "The value of the operands have to be numbers.")

    def Add(self, operands):
        """
            Takes a numbers separated by comma as a string and performs mathematical 
            addition on them and returns the result.
        """
        # If its not a string raise value error.
        if not isinstance(operands, str):
            raise InvalidValueException(
                "The operands have to be numbers separate by comma.")

        # If it is empty string or none return 0.
        if not operands:
            return 0

        # If it is empty string or none return 0.
        numbers = self._to_number(operands)

        return sum(numbers)
