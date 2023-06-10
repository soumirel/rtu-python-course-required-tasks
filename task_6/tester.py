from test_data import TestData


class Tester:
    def __init__(self, data_handler):
        self.data_handler = data_handler

        self.test_data = [
            TestData([2017, 'IOKE', 'QMAKE', 1968], 9),
            TestData([2017, 'COBOL', 'TWIG', 1980], 1),
            TestData([2017, 'SASS', 'QMAKE', 1980], 4),
            TestData([2019, 'SASS', 'QMAKE', 1968], 5),
            TestData([2019, 'SASS', 'COOL', 1968], 6)
        ]

    def test(self):
        for i in range(0, len(self.test_data)):
            if self.data_handler(self.test_data[i].source) != self.test_data[i].answer:
                print('test ' + str(i) + ' failed')


