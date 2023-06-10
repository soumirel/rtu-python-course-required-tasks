from tester import Tester


def main(x: list) -> int:
    graph = [
        ['2019', 'COBOL', '', '1980'],  # 0
        ['2017', 'COBOL', '', '1980'],  # 1
        ['', 'IOKE', '', '1980'],  # 2
        ['2019', 'SASS', '', '1980'],  # 3
        ['2017', 'SASS', '', '1980'],  # 4
        ['2019', '', 'QMAKE', '1968'],  # 5
        ['2019', '', 'COOL', '1968'],  # 6
        ['2019', '', 'TWIG', '1968'],  # 7
        ['2017', 'COBOL', '', '1968'],  # 8
        ['2017', 'IOKE', '', '1968'],  # 9
        ['2017', 'SASS', '', '1968'],  # 10
    ]

    graph_length = len(graph)

    for external_iter in range(0, graph_length):
        current_branch = graph[external_iter]
        is_good_branch = True
        for internal_iter in range(0, min(len(current_branch), len(x))):
            branch_token = current_branch[internal_iter]
            x_token = str(x[internal_iter])
            if not (branch_token == x_token or branch_token == ''):
                is_good_branch = False
                break
        if is_good_branch:
            return external_iter

    return 0


if __name__ == '__main__':
    tester = Tester(main)
    tester.test()
