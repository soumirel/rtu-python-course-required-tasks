from struct import *


def main(source):
    a = {}

    global_address = 5

    a['A1'] = unpack_from('>q', source, global_address)[0]
    global_address += 8

    a['A2'] = unpack_from('>i', source, global_address)[0]
    global_address += 4

    a['A3'] = unpack_from('>h', source, global_address)[0]
    global_address += 2

    a4 = {}
    b_address = unpack_from('>I', source, global_address)[0]
    global_address += 4

    a4['B1'] = unpack_from('>B', source, b_address)[0]
    b_address += 1

    a4['B2'] = unpack_from('>d', source, b_address)[0]
    b_address += 8

    b3 = []
    b3_size = 8
    for b3_iter in range(b3_size):
        b3.append(unpack_from('>I', source, b_address)[0])
        b_address += 4
    a4['B3'] = b3

    a4['B4'] = unpack_from('>H', source, b_address)[0]
    b_address += 2

    a4['B5'] = unpack_from('>q', source, b_address)[0]
    b_address += 8

    b6_size = unpack_from('>I', source, b_address)[0]
    b_address += 4
    b6_address = unpack_from('>H', source, b_address)[0]
    b_address += 2
    b6 = []
    for b6_iter in range(b6_size):
        c = {'C1': unpack_from('>H', source, b6_address)[0]}
        b6_address += 2
        c['C2'] = unpack_from('>h', source, b6_address)[0]
        b6_address += 2
        c['C3'] = unpack_from('>H', source, b6_address)[0]
        b6_address += 2
        b6.append(c)
    a4['B6'] = b6

    a4['B7'] = unpack_from('>H', source, b_address)[0]
    b_address += 2

    b8 = {'D1': unpack_from('>i', source, b_address)[0]}
    b_address += 4

    b8['D2'] = unpack_from('>f', source, b_address)[0]
    b_address += 4

    d3_size = unpack_from('>H', source, b_address)[0]
    b_address += 2
    d3_address = unpack_from('>H', source, b_address)[0]
    b_address += 2
    d3 = []
    for d3_iter in range(d3_size):
        d3.append(unpack_from('>i', source, d3_address)[0])
        d3_address += 4
    b8['D3'] = d3

    b8['D4'] = unpack_from('>Q', source, b_address)[0]
    b_address += 8

    b8['D5'] = unpack_from('>i', source, b_address)[0]
    b_address += 4

    b8['D6'] = unpack_from('>h', source, b_address)[0]
    b_address += 2

    b8['D7'] = unpack_from('>Q', source, b_address)[0]
    b_address += 8

    b8['D8'] = unpack_from('>I', source, b_address)[0]
    b_address += 4
    a4['B8'] = b8

    a['A4'] = a4

    a5_address = unpack_from('>H', source, global_address)[0]
    global_address += 2
    a5 = {}

    e1_size = unpack_from('>H', source, a5_address)[0]
    a5_address += 2
    e1_address = unpack_from('>H', source, a5_address)[0]
    a5_address += 2
    e1 = []
    for e1_iter in range(e1_size):
        e1.append(unpack_from('>b', source, e1_address)[0])
        e1_address += 1
    a5['E1'] = e1

    a5['E2'] = unpack_from('>B', source, a5_address)[0]
    a5_address += 1

    a5['E3'] = unpack_from('>I', source, a5_address)[0]
    a5_address += 4

    a['A5'] = a5

    return a

