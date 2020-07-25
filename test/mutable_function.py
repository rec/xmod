import xmod


@xmod(mutable=True)
def mutable_function():
    return FOO


FOO = 23
BAR = 99
