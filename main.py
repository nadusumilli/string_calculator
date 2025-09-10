
class StringCalculator:
    """
        String Calculator, performs mathematical calculations on strings.
    """

    def __init__(self):
        self.delimeter = "\n"

    def _to_number(self, operands):
        result = []
        try:
            if isinstance(operands, list):
                result.extend([float(x) if "." in x else int(x)
                              for x in operands])
            else:
                result.append(float(operands)
                              if "." in operands else int(operands))
        except ValueError:
            raise ValueError(
                "The value of the operands have to be numbers.")
        return result

    def Add(self, operands):
        """
            Takes a numbers separated by comma as a string and performs mathematical 
            addition on them and returns the result.
        """
        # If its not a string raise value error.
        if not isinstance(operands, str):
            raise ValueError(
                "The operands have to be numbers separate by comma.")

        # If it is empty string or none return 0.
        if not operands:
            return 0

        # If it is empty string or none return 0.
        if "," not in operands:
            result = self._to_number(operands)
            return result[0]

        numbers = self._to_number(operands.split(self.delimeter))

        return sum(numbers)
