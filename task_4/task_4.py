def main(n):
    if n == 0:
        return -0.88
    elif n == 1:
        return 0.82
    else:
        return (main(n - 1) - 78 * main(n - 2) ** 2 - 48) \
            / 78 + 1
