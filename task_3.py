from math import sin


def main(a, n, x):
    result = 0
    for k in range(1, n + 1):
        for j in range(1, a + 1):
            result += (abs(1 + (k ** 2) / 42 + 95 * j) ** 6) \
                      - 85 * sin((x ** 2) / 82) ** 4
    return result
