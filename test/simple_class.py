import xmod

TEST = 5


class SimpleClass:
    def __call__(self, a, b):
        return a, b

    def __iter__(self):
        return iter((2, 3))


xmod(SimpleClass(), full=True)
