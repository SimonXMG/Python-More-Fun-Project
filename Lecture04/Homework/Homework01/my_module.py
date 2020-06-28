import math

def compute(numbers):
    result = []
    for n in numbers:
        result.append(math.factorial(n))
    return result