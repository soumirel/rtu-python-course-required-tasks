import re


def main(table):
    table = [[cell for cell in row if cell is not None]
             for row in table if any(row)]
    transposed_table = [list(row) for row in zip(*table)]

    transposed_table[0] = \
        [str(round(float(item), 1)) for item in transposed_table[0]]

    name_pattern = re.compile(r"(\w+)\s(\w)\.\s(\w+)")
    transposed_table[1] = \
        [name_pattern.sub(r"\3 \1", cell)
         for cell in transposed_table[1]]

    email_pattern = re.compile(r"\[at]")
    transposed_table[2] = \
        [email_pattern.sub("@", cell)
         for cell in transposed_table[2]]

    return transposed_table


print(main([[0.74, 'Мирослав Г. Фирев', None, None, 'miroslav78[at]rambler.ru'],
            [0.90, 'Вадим У. Морак', None, None, 'vadim4[at]yandex.ru'],
            [None, None, None, None, None],
            [0.43, 'Сергей Ч. Нокунман', None, None, 'nokunman8[at]yandex.ru'],
            [None, None, None, None, None],
            [0.23, 'Георгий К. Шонодий', None, None, 'georgij73[at]mail.ru']]))
