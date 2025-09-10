
class StringCalculator:
    """
        String Calculator, performs mathematical calculations on strings.
    """

    def __init__(self):
        pass

    def Add(self, operands):
        """
            Takes a numbers separated by comma as a string and performs mathematical 
            addition on them and returns the result.
        """
        # If its not a string raise value error.
        if not isinstance(operands, str):
            print("\n\n\n\n", operands)
            raise ValueError(
                "The operands have to be numbers separate by comma.")

        # If it is empty string or none return 0.
        if not operands:
            return 0

        # If it is empty string or none return 0.
        if "," not in operands:
            result = 0
            try:
                result = int(operands)
            except ValueError:
                raise ValueError(
                    "The value of the operands have to be numbers.")
            return result

        numbers = operands.split(",")

        return int(numbers[0]) + int(numbers[1])
