"""
    Author: Dan Shaw
    Title: CustomMath
    Desc: Contains custom math and validation functions
"""

class Validation:
    # Validates whether inputQuery is a valid number by trying to convert to a float
    # Returns the converted float if successfull and None if fails
    def validateFloat(inputQuery):
        try:
            return float(inputQuery)
        except:
            return None

    # NOTE I spent so long trying to figure out why this function actually works because converting a decimal number to an int shouldn't throw an exception at all, then I realized trying to convert a STRING with a decimal to an int will throw a ValueError
    # Attempts to convert value to int. If successful, returns the converted value
    # If fails, returns None
    def validateInt(value):
        try:
            return int(value)
        except ValueError:
            return None
