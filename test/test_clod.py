import unittest


class TestClod(unittest.TestCase):
    def test_simple_function(self):
        from . import simple_function

        assert simple_function() == 23
        assert simple_function.BAR == 99

    def test_simple(self):
        from . import simple_class

        assert simple_class(7, 12) == (7, 12)
        assert list(simple_class) == [2, 3]
        simple_class.boing = 'bang'
        assert simple_class.boing == 'bang'

    def test_builtin(self):
        from . import builtin

        assert builtin == []
        builtin.append(2)

        assert builtin == [2]

    def test_decorator(self):
        from . import decorator

        assert decorator() == 23
        assert decorator.BAR == 99

    def test_decorator_with_parameter(self):
        from . import decorator_with_parameter

        assert decorator_with_parameter() == 23
        assert decorator_with_parameter.BAR == 99
