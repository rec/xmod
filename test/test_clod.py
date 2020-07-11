import unittest


class TestClod(unittest.TestCase):
    def test_function(self):
        from . import foo

        assert foo() == 23
        assert foo.BAR == 99

    def test_simple(self):
        from . import foo2

        assert foo2(7, 12) == (7, 12)
        assert list(foo2) == [2, 3]
        foo2.boing = 'bang'
        assert foo2.boing == 'bang'

    def test_builtin(self):
        from . import foo3

        assert foo3 == []
        foo3.append(2)

        assert foo3 == [2]
