def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers")
    return float(a) + float(b)


def subtract(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def divide(a, b, ndigits=None):
    if float(b) == 0.0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = float(a) / float(b)
    if ndigits is not None:
        return round(result, ndigits)
    return result


def mean(values):
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(values):
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    if n == 0:
        raise ValueError("median() requires at least one value")
    mid = n // 2
    if n % 2 == 1:
        return sorted_vals[mid]
    return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


def variance(values, sample=False):
    n = len(values)
    if n < 2:
        raise ValueError("variance() requires at least two values")
    m = mean(values)
    ss = sum((float(x) - m) ** 2 for x in values)
    return ss / (n - 1 if sample else n)
