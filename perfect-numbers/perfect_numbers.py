def get_divisors_from_number(number):
    return [n for n in range(1, number) if number % n == 0]


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = get_divisors_from_number(number)
    aliquot_sum = sum(divisors)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"
