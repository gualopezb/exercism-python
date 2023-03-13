def is_armstrong_number(number):
    string_number = str(number)
    number_length = len(string_number)
    return sum(pow(int(i), number_length) for i in string_number) == number
