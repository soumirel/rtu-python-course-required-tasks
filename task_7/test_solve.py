def main(source):
    source = bin(source)[2:].zfill(24)
    print(source)
    x_dict = {
        'X6': int(source[0:7], 2),
        'X5': int(source[7:8], 2),
        'X4': int(source[8:11], 2),
        'X3': int(source[11:14], 2),
        'X2': int(source[14:22], 2),
        'X1': int(source[22:], 2)
    }
    x_dict_1 = {
        'X6': source[0:7],
        'X5': source[7:8],
        'X4': source[8:11],
        'X3': source[11:14],
        'X2': source[14:22],
        'X1': source[22:]
    }
    print(x_dict_1)
    print(x_dict)
    print(bin(x_dict['X2'] << 3 | x_dict['X4']))
    answer = int(
        (((x_dict['X4'] << 2 |
           x_dict['X1']) << 1 |
          x_dict['X5']) << 7 |
         x_dict['X6']) << 3 |
        x_dict['X3']
    )
    return answer


if __name__ == '__main__':
    print(main(15162321))
