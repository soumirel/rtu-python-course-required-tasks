class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def close(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'E':
            self.state = 'F'
            return 5
        raise MealyError('close')

    def look(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        elif self.state == 'D':
            self.state = 'E'
            return 4
        elif self.state == 'E':
            return 7
        elif self.state == 'F':
            self.state = 'A'
            return 8
        raise MealyError('look')

    def paint(self):
        if self.state == 'E':
            self.state = 'C'
            return 6
        elif self.state == 'B':
            self.state = 'F'
            return 2
        raise MealyError('paint')


def main():
    return StateMachine()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    raises(lambda: o.look(), MealyError)
    raises(lambda: o.paint(), MealyError)
    assert o.close() == 0
    raises(lambda: o.close(), MealyError)
    assert o.look() == 1
    assert o.close() == 3
    assert o.look() == 4
    assert o.paint() == 6
    assert o.close() == 3
    assert o.look() == 4
    assert o.look() == 7
    assert o.close() == 5
    assert o.look() == 8
    assert o.close() == 0
    assert o.paint() == 2
