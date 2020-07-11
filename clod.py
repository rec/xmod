r"""
🌱 - clod: replace your module with an object - 🌱
===========================================================

Replace your module with an object, allowing for example "modules" that you can
call or index.

"""

__all__ = ('clod',)

import functools
import sys

__version__ = '0.9.0'

MODULE_VARIABLES = {
    '__all__',
    '__cached__',
    '__doc__',
    '__file__',
    '__loader__',
    '__name__',
    '__package__',
    '__path__',
    '__spec__',
}

NO_COPY = {
    '__class__',
    '__getattr__',
    '__getattribute__',
    '__init__',
    '__init_subclass__',
    '__new__',
    '__setattr__',
}


def clod(rep, name, variables=MODULE_VARIABLES, no_copy=NO_COPY):
    def method(f):
        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            return f(*args, **kwargs)

        return wrapped

    original = sys.modules[name]
    members = {'_clod_wrapped': original}

    for attr in dir(rep):
        if attr not in NO_COPY:
            value = getattr(rep, attr)
            if callable(value):
                value = method(value)
            members[attr] = value

    if callable(rep):
        members['__call__'] = method(rep)

    members['__getattr__'] = method(original.__getattribute__)
    members['__setattr__'] = method(original.__setattr__)

    none = object()
    for k in MODULE_VARIABLES:
        v = getattr(original, k, none)
        if v is not none:
            members[k] = v

    sys.modules[name] = type(name, (object,), members)()
    return original, sys.modules[name]


clod(clod, __name__)
