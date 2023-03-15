def is_triangle(sides):
    if len(sides) != 3:
        return False
    [a, b, c] = sides
    return all(side > 0 for side in sides) and a + b >= c and b + c >= a and a + c >= b


def equilateral(sides):
    if not is_triangle(sides):
        return False
    [a, b, c] = sides
    return a == b and b == c


def isosceles(sides):
    if not is_triangle(sides):
        return False
    [a, b, c] = sides
    return a == b or b == c or a == c


def scalene(sides):
    if not is_triangle(sides):
        return False
    [a, b, c] = sides
    return a != b and b != c and a != c
