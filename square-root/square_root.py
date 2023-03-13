def square_root(number):
    k = 0
    s = 0
    while s <= number:
        s = (2 * k) + s + 1
        k = k + 1
    return k - 1
