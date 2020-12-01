import xmod

TEST = 5


@xmod
class ActualClass:
    def __call__(self, a, b):
        return a, b

    def __iter__(self):
        return iter((2, 3))
