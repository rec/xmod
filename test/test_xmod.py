import unittest


class TestXmod(unittest.TestCase):
    def test_simple_function(self):
        from . import simple_function

        assert simple_function() == 23
        assert simple_function.BAR == 99

    def test_dir(self):
        from . import actual_class

        actual = dir(actual_class)
        expected = [
            'ActualClass',
            'TEST',
            '__builtins__',
            '__cached__',
            '__call__',
            '__doc__',
            '__file__',
            '__getattr__',
            '__loader__',
            '__name__',
            '__package__',
            '__setattr__',
            '__spec__',
            '_xmod_extension',
            '_xmod_wrapped',
            'xmod',
        ]
        assert actual == expected

    def test_dir2(self):
        from . import simple_function

        actual = dir(simple_function)
        expected = [
            'BAR',
            '__builtins__',
            '__cached__',
            '__call__',
            '__doc__',
            '__file__',
            '__getattr__',
            '__loader__',
            '__name__',
            '__package__',
            '__setattr__',
            '__spec__',
            '_xmod_extension',
            '_xmod_wrapped',
            'simple_function',
            'xmod',
        ]

        assert actual == expected

    def test_simple(self):
        from . import simple_class

        assert simple_class(7, 12) == (7, 12)
        assert list(simple_class) == [2, 3]
        simple_class.boing = 'bang'
        assert simple_class.boing == 'bang'

    def test_error(self):
        import xmod

        with self.assertRaises(ValueError) as m:
            xmod(3, name=__name__, full=False)
        actual = m.exception.args[0]
        expected = 'extension must be callable if full is False'
        assert actual == expected

    def test_list(self):
        from . import looks_like_list

        assert looks_like_list == []
        looks_like_list.append(2)

        assert looks_like_list == [2]

        looks_like_list[:] = range(3)
        looks_like_list[0] = 'a'
        assert looks_like_list == ['a', 1, 2]
        assert len(looks_like_list) == 3

    def test_decorator_no_parameter(self):
        from . import decorator

        assert decorator() == 23
        assert decorator.BAR == 99

    def test_decorator_with_parameter(self):
        from . import decorator_with_parameter

        assert decorator_with_parameter() == 23
        assert decorator_with_parameter.BAR == 99
