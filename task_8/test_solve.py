def main(source: str):
    answer = []
    keys_ind = {
        'q(' : 0,
        ')' : 0
    }
    vals_ind = {
        '::=': 0,
        ';' : 0
    }
    has_next = True
    while True:
        key = source[
            source.find('q(', keys_ind['q(']) + len('q('):
              source.find(')', keys_ind[')']) + len(')') - 1
        ]
        if source.find('q(', keys_ind['q(']) != -1:
            keys_ind['q('] = source.find('q(', keys_ind['q(']) + len('q(')
            keys_ind[')'] = source.find(')', keys_ind[')']) + len(')')
        else:
            break
        val = source[
            source.find('::=', vals_ind['::=']) + len('::=') :
                source.find(';', vals_ind[';']) + len(';') - 1
        ]
        vals_ind['::='] = source.find('::=', vals_ind['::=']) + len('::=')
        vals_ind[';'] = source.find(';', vals_ind[';']) + len(';')
        val = val.strip()
        answer.append((key, int(val)))
    return answer


if __name__ == '__main__':
    print(main('.do .begin let q(lalaar_464) ::= -9498;.end, .begin let q(veteen_740) ::= -8778;.end,.begin let q(atzage_640)::= 4249; .end, .begin let q(qubiqu_501) ::=2099; .end, .end'))
