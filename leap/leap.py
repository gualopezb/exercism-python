def leap_year(year):
    divisible_by_4 = year % 4 == 0
    divisible_by_100 = year % 100 == 0
    divisible_by_400 = year % 400 == 0

    if not divisible_by_100:
        return divisible_by_4
    return divisible_by_4 and divisible_by_400
