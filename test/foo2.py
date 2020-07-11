import clod

TEST = 5


class Foo:
    def __call__(self, a, b):
        return a, b

    def __iter__(self):
        return iter((2, 3))


clod(Foo(), __name__)
