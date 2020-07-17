r"""
🌱 - clod: CLass mODule! Give your module the power of an object - 🌱
=========================================================================

_Give your module the power of an object, with ``clod``._

Ever wanted to call a module directly, or index it?
Or just sick of seeing ``from foo import foo`` in your examples?

``clod`` is a tiny library that solves both these issues in one line of code,
by extending a module with the methods and members of a Python object.

This is extremely handy for modules that primarily do one thing,
and little else.

EXAMPLE:

``foo.py``:

.. code-block:: python

    import clod

    # ...

    def foo(*args, **kwargs):
        return args, kwargs

    clod(foo)


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

OMIT = {
    '__class__',
    '__getattr__',
    '__getattribute__',
    '__init__',
    '__init_subclass__',
    '__new__',
    '__setattr__',
}

WRAPPED_ATTRIBUTE = '_clod_wrapped'


def clod(extension=None, name=None, variables=None, omit=None):
    """
    Extend the system module at ``name`` with an object.

    ARGUMENTS
      extension

    """

    def method(f):
        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            return f(*args, **kwargs)

        return wrapped

    if extension is None:
        # It's a decorator with properties
        assert name is not None or omit is not None or variables is not None
        return functools.partial(
            clod, name=name, variables=variables, omit=omit
        )

    name = extension.__module__ if name is None else name
    variables = MODULE_VARIABLES if variables is None else variables
    omit = OMIT if omit is None else omit

    original = sys.modules[name]
    members = {WRAPPED_ATTRIBUTE: original}

    for attr in dir(extension):
        if attr not in omit:
            value = getattr(extension, attr)
            if callable(value):
                value = method(value)
            members[attr] = value

    if callable(extension):
        members['__call__'] = method(extension)

    members['__getattr__'] = method(original.__getattribute__)
    members['__setattr__'] = method(original.__setattr__)

    none = object()
    for k in variables:
        v = getattr(original, k, none)
        if v is not none:
            members[k] = v

    sys.modules[name] = type(name, (object,), members)()
    return extension


clod(clod)
