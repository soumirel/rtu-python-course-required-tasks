def main(x: list) -> int:
    tree = {
        '2017': {
            'COBOL': {
                '1980': 1,
                '1968': 8
            },
            'IOKE': {
                '1980': 2,
                '1968': 9
            },
            'SASS': {
                '1980': 4,
                '1968': 10
            }
        },
        '2019': {
            '1980': {
                'COBOL': 0,
                'IOKE': -1,
                'SASS': 3
            },
            '1968': {
                'QMAKE': 5,
                'COOL': 6,
                'TWIG': 7
            },
        }
    }

    value = tree
    while True:
        for argument in x:
            if type(value) is int:
                return value
            new_value = value.get(str(argument))
            if new_value is not None:
                value = new_value


if __name__ == '__main__':
    print(main([2019, 'COBOL', 'TWIG', 1980]))

