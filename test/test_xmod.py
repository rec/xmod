import unittest


class TestXmod(unittest.TestCase):
    def test_simple_function(self):
        from . import simple_function

        assert simple_function() == 23
        assert simple_function.BAR == 99

    def test_dir(self):
        from . import actual_class

        dir(actual_class)

    def test_simple(self):
        from . import simple_class

        assert simple_class(7, 12) == (7, 12)
        assert list(simple_class) == [2, 3]
        simple_class.boing = 'bang'
        assert simple_class.boing == 'bang'

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
