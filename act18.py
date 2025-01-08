# documentation strings/ docstrings

# this function is for calculating factorial

def factorial(number):
    """ this function is for calculating factorial, just put th
    e number inside the parenthesis """

    fact = 1
    for x in range(number, 0, -1):
        fact *= x

    return fact
