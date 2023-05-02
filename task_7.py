def main(d):
    trunc_d = {
        'K5': int('0b' + bin(int(d['K5'], 16))[2:].zfill(7)[-7:], 2),
        'K4': int('0b' + bin(int(d['K4'], 16))[2:].zfill(3)[-3:], 2),
        'K3': int('0b' + bin(int(d['K3'], 16))[2:].zfill(1)[-1:], 2),
        'K2': int('0b' + bin(int(d['K2'], 16))[2:].zfill(1)[-1:], 2),
        'K1': int('0b' + bin(int(d['K1'], 16))[2:].zfill(3)[-3:], 2)
    }
    answer = ((((trunc_d['K5'] << 3 |
                 trunc_d['K4']) << 1 |
                trunc_d['K3']) << 1 |
               trunc_d['K2']) << 3 |
              trunc_d['K1'])
    return hex(answer)


print(main({'K1': '0x2', 'K2': '0x1', 'K3': '0x0', 'K4': '0x4', 'K5': '0x5a'}))