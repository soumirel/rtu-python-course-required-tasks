import re

def main(data_string):
    regexp = r'loc\s*"(?P<name>\w+)"\s*<\|\s*\{(?P<values>[^}]*)\}'
    matches = re.finditer(regexp, data_string)
    result = []
    for match in matches:
        name = match.group('name')
        values_str = match.group('values')
        values = [value.strip() for value in values_str.split(';')]
        result.append((name, values))
    return result


print(main(""".do{{ loc "inorma" <| { reer_396 ; orzare ; mage_341 ;enti}}}. {{ loc
"reat_903"<| { anbi_755; bite_368; mausar_527 ; esgequ}}}. {{ loc
"rausxe" <| {anbidi ; veindi; soxe } }}. {{loc"quedbi"<| {orgean_565
;isra_434 } }}. .end"""))