from math import cos


def main(x, y):
    numerator = pow((x + pow(y, 2) + pow(y, 3)), 2) -\
                14 * abs(x + 80 * pow(x, 3))
    denominator = 51 * pow(abs(26 * y), 2) + pow(x, 7)
    left = numerator / denominator
    right = pow(cos(25 + 37 * pow(x, 3) + y), 4)
    return left - right
