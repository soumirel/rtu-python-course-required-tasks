def main(x, y):
    length = len(x)
    result = 0
    for i in range(0, length):
        result += (x[i] + 89 * y[length - 1 - i] ** 3 + 1) ** 2
    return result
