import unittest


class TestXmod(unittest.TestCase):
    def test_simple_function(self):
        from .modules import simple_function

        assert simple_function() == 23
        assert simple_function.BAR == 99

    def test_dir(self):
        from .modules import actual_class

        actual = dir(actual_class)
        expected = ['ActualClass', 'TEST'] + COMMON + ['xmod']
        assert actual == expected

    def test_dir2(self):
        from .modules import simple_function

        actual = dir(simple_function)
        expected = ['BAR'] + COMMON + ['simple_function', 'xmod']
        assert actual == expected

    def test_mutable(self):
        from .modules import mutable_function

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

    def test_mutable_class(self):
        from .modules import mutable_class as mc

        assert mc.one() == 19
        # assert mc.onep == 19

        mc.ONE = 32
        assert mc.one() == 32
        # assert mc.onep == 32

        assert mc.two() == 12
        mc.TWO = 23
        assert mc.two() == 23
        # assert mc.twop == 12

        # del mc.TWO
        # with self.assertRaises(AttributeError):
        #     mc.two()

        # with self.assertRaises(AttributeError):
        #     mc.twop

    def test_simple(self):
        from .modules import simple_class

        assert simple_class(7, 12) == (7, 12)
        assert list(simple_class) == [2, 3]
        with self.assertRaises(TypeError) as m:
            simple_class.boing = 'bang'
        assert m.exception.args[0].startswith('Class is immutable')

    def test_error(self):
        import xmod

        with self.assertRaises(ValueError) as m:
            xmod(3, name=__name__, full=False)
        actual = m.exception.args[0]
        expected = 'extension must be callable if full is False'
        assert actual == expected

    def test_list(self):
        from .modules import looks_like_list

        assert looks_like_list == []
        looks_like_list.append(2)

        assert looks_like_list == [2]

        looks_like_list[:] = range(3)
        looks_like_list[0] = 'a'
        assert looks_like_list == ['a', 1, 2]
        assert len(looks_like_list) == 3

    def test_decorator_no_parameter(self):
        from .modules import decorator

        assert decorator() == 23
        assert decorator.BAR == 99

    def test_decorator_with_parameter(self):
        from .modules import decorator_with_parameter

        assert decorator_with_parameter() == 23
        assert decorator_with_parameter.BAR == 99

    def test_partial_function(self):
        from .modules import partial_function

        assert partial_function(1, 2) == (0, 1, 2, 3)

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
