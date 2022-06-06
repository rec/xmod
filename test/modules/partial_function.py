import functools
import xmod


def base(a, b, c, d):
    return a, b, c, d


xmod(functools.partial(base, 0, d=3))
