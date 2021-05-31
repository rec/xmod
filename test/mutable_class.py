# import xmod

ONE = 19


class MutableClass:
    TWO = 12

    def one(self):
        return ONE

    def two(self):
        return self.TWO

    @property
    def onep(self):
        return ONE

    @property
    def twop(self):
        return self.TWO


# xmod(MutableClass(), full=True, mutable=True)
