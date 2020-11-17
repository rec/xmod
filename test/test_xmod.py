import unittest


class TestXmod(unittest.TestCase):
    def test_simple_function(self):
        from . import simple_function

        assert simple_function() == 23
        assert simple_function.BAR == 99

    def test_dir(self):
        from . import actual_class

        actual = dir(actual_class)
        expected = ['ActualClass', 'TEST'] + COMMON + ['xmod']
        assert actual == expected

    def test_dir2(self):
        from . import simple_function

        actual = dir(simple_function)
        expected = ['BAR'] + COMMON + ['simple_function', 'xmod']
        assert actual == expected

    def test_mutable(self):
        from . import mutable_function

        assert mutable_function() == 23
        assert mutable_function.FOO == 23
        assert mutable_function.BAR == 99
        assert not hasattr(mutable_function, 'BAZ')

        mutable_function.FOO = 32
        del mutable_function.BAR
        mutable_function.BAZ = 5

        assert mutable_function() == 32
        assert mutable_function.FOO == 32
        assert not hasattr(mutable_function, 'BAR')
        assert mutable_function.BAZ == 5

    def test_simple(self):
        from . import simple_class

        assert simple_class(7, 12) == (7, 12)
        assert list(simple_class) == [2, 3]
        with self.assertRaises(TypeError) as m:
            simple_class.boing = 'bang'
        assert m.exception.args[0] == 'Class is immutable'

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


COMMON = [
    '__builtins__',
    '__cached__',
    '__call__',
    '__delattr__',
    '__dir__',
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
]
