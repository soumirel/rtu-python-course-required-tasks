class TestData:
    def __init__(self, source, answer):
        self.source = source
        self.answer = answer


class Tester:
    def __init__(self, data_handler):
        self.data_handler = data_handler

        self.test_data = [
            TestData(source=b'YKQ\x00\x00\x00\x02\x00\x00\x00c\xf3\x06\x00e3\\a\xd6\x00\x00\x00\x07\x00'
                            b'\x00\x00nM"\x00u\x0fY,\xfa?\x07#[\xd5\xa7p\xd8\x19}S\xe7\x00\x08\x00\x00\x00'
                            b"~D'\xe1\xfd\xe2}\xbf\xd2\xcb\x98\x99\xe73l\x9d\x87\xb4\x11n\xc7-G4\x02G-\xc2"
                            b'\n\xde\x1d\xc8\xf9\x95\x9d"\xf2\xe7uy\x9f\x18\x8bBAJ\xc5P\xc6Q?K'
                            b'\x8d\x11D\x85\x85C\x88\xfa\xa3\xa3\xa9E\xdez>^gh\x9ec\xa32hmupddsm',
                     answer={'A1': [{'B1': {'C1': [80, -58], 'C2': 62214},
                                     'B2': {'D1': 81, 'D2': 0.7951212525367737, 'D3': 17541, 'D4': -31421},
                                     'B3': 861692374},
                                    {'B1': {'C1': [-120, -6, -93, -93, -87, 69, -34], 'C2': 19746},
                                     'B2': {'D1': 122,
                                            'D2': 0.21719133853912354,
                                            'D3': -24989,
                                            'D4': -23758},
                                     'B3': 257502458}],
                             'A2': 0.5278832316398621,
                             'A3': -3051346149077330969,
                             'A4': 'hmupddsm',
                             'A5': 1143464445,
                             'A6': 57981,
                             'A7': -0.2936765196762312,
                             'A8': [-7095504700932936377,
                                    3747636101780266525,
                                    -3964973494794262667,
                                    8763750386277370565]}
                     ),
            TestData(source=b'YKQ\x00\x00\x00\x05\x00\x00\x00c\xb8\xe7\x00h\x8c\xa2`\xc3\x00'
                            b'\x00\x00\x05\x00\x00\x00q?q\x00v}\x11\xaf\xa1>\xf1\x00/\xf1!\x01K)'
                            b'\x80[\xda\x00\x06\x00\x00\x00\x7f\xfa$?6\xb2\x8b\xbf\xe4w`C\xe4gl$~9\x05n'
                            b'uk$\xa9F>\xc5W\xcc\xd4-\x13\xf2OzJ~|\xdc\x12\x82\xad\x9b\xb2\xfboO\x06'
                            b'Iqd\xbc\xa0\xbf\rEW%\xfd\xcc\xee\xbf\x96\x80k\x00\xab\xbe\x16Isp'
                            b'\xe6\xd7\x8eveputk',
                     answer={'A1': [{'B1': {'C1': [6, 73, 113, 100, -68], 'C2': 47335},
                                     'B2': {'D1': -96, 'D2': -0.551839292049408,
                                            'D3': 9725, 'D4': -13074},
                                     'B3': -1935515453},
                                    {'B1': {'C1': [-65, -106, -128, 107, 0], 'C2': 16241},
                                     'B2': {'D1': -85,
                                            'D2': -0.14676456153392792,
                                            'D3': 28902,
                                            'D4': -10354},
                                     'B3': 2098311073}],
                             'A2': 0.4707045257091522,
                             'A3': -1071573814007014438,
                             'A4': 'veputk',
                             'A5': -98287818,
                             'A6': 45707,
                             'A7': -0.6395722700137703,
                             'A8': [2629601927921756964,
                                    -6249238415627463635,
                                    1437298617739017436,
                                    1333819323889446735]})
        ]

    def test(self):
        for test_data in self.test_data:
            assert self.data_handler(test_data.source) == test_data.answer


