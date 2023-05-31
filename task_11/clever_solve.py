from struct import unpack_from, calcsize

from tester import Tester


class Types:
    uint16 = 'H'
    int16 = 'h'
    char = 'c'
    float = 'f'
    int8 = 'b'
    int64 = 'q'
    uint64 = 'Q'
    uint32 = 'I'
    int32 = 'i'
    double = 'd'


class BinaryReader:
    def __init__(self, data, offset, order='>'):
        self.data = data
        self.offset = offset
        self.order = order

    def get_reader_on_address(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.int8)
    d2 = reader.read(Types.float)
    d3 = reader.read(Types.int16)
    d4 = reader.read(Types.int16)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def read_c(reader):
    c1_size = reader.read(Types.uint32)
    c1_address = reader.read(Types.uint32)
    c1_reader = reader.get_reader_on_address(c1_address)
    c1 = [c1_reader.read(Types.int8) for _ in range(c1_size)]
    c2 = reader.read(Types.uint16)
    return dict(C1=c1, C2=c2)


def read_b(reader):
    b1 = read_c(reader)
    b2_address = reader.read(Types.uint16)
    b2_reader = reader.get_reader_on_address(b2_address)
    b2 = read_d(b2_reader)
    b3 = reader.read(Types.int32)
    return dict(B1=b1, B2=b2, B3=b3)


def read_a(reader):
    a1_size = 2
    a1 = [read_b(reader) for _ in range(a1_size)]
    a2 = reader.read(Types.float)
    a3 = reader.read(Types.int64)
    a4_size = reader.read(Types.uint16)
    a4_address = reader.read(Types.uint32)
    a4_reader = reader.get_reader_on_address(a4_address)
    a4 = ''.join(a4_reader.read(Types.char).decode() for _ in range(a4_size))
    a5 = reader.read(Types.int32)
    a6 = reader.read(Types.uint16)
    a7 = reader.read(Types.double)
    a8_size = 4
    a8 = [reader.read(Types.int64) for _ in range(a8_size)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5,
                A6=a6, A7=a7, A8=a8)


def main(data):
    return read_a(BinaryReader(data, 3))


if __name__ == '__main__':
    tester = Tester(main)
    tester.test()
