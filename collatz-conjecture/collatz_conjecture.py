def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    total_steps = 0
    current_number = number
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = current_number / 2
        else:
            current_number = (current_number * 3) + 1
        total_steps += 1
    return total_steps
