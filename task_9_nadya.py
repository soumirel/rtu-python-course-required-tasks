import re


def main(table):
    transposed_table = [list(row) for row in zip(*table)]
    clear_transposed_table = []
    for i in range(0, len(transposed_table)):
        if transposed_table[i] not in clear_transposed_table \
                and transposed_table[i][0] is not None:
            clear_transposed_table.append(transposed_table[i])

    clear_transposed_table[0] = [
        cropped[3:] for cropped in clear_transposed_table[0]
    ]

    dates = []
    surnames = []
    regexp = r'(\d{2})/(\d{2})/(\d{2})&(.+)'
    for i in range(0, len(clear_transposed_table[1])):
        match = re.search(regexp, clear_transposed_table[1][i])
        if match:
            day, month, year, name = match.groups()
            dates.append(f"{year}.{month}.{day}")
            surnames.append(name.split()[0])
    clear_transposed_table[1] = dates
    clear_transposed_table[2] = ["Выполнено" if elem == 'Y' else "Не выполнено"
                                 for elem in clear_transposed_table[2]]
    clear_transposed_table.append(surnames)
    return [list(row) for row in zip(*clear_transposed_table)]


# Ниже - тестирование. Вставляй только main и import re, ты знаешь
source_table = [["+7 802 212-7614", None, "03/12/04&Вовишук В.Ф.", "N", "N"],
                ["+7 934 836-0482", None, "26/03/04&Засич Т.Т.", "N", "N"],
                ["+7 310 161-1152", None, "04/09/04&Кобский Д.З.", "Y", "Y"],
                ["+7 562 007-6869", None, "05/09/99&Венский Р.З.", "Y", "Y"]]

processed_table = [["802 212-7614", "04.12.03", "Не выполнено", "Вовишук"],
                   ["934 836-0482", "04.03.26", "Не выполнено", "Засич"],
                   ["310 161-1152", "04.09.04", "Выполнено", "Кобский"],
                   ["562 007-6869", "99.09.05", "Выполнено", "Венский"]]

assert main(source_table) == processed_table
