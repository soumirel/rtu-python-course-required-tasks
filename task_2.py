import math


def main(y):
    if (y < 147):
        return 48 * y**4 + y**5 + 1
    elif (y < 173):
        return 97 * y**3 + 67 + (math.floor(y)) ** 7
    elif (y < 256):
        return y + 47 * (78 * y**2 + 27*y)**6
    else:
        first = ((y**3 - 1 - y) ** 0.5) / 74
        second = 84 * (y + 25 * y **3)**3
        third = 79 * (98 * y + y**3 + y**2)**5
        return first + second + third
