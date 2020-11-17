"""
🌱 - xmod: Extend a module with any Python object - 🌱
=========================================================================

Callable modules!  Indexable modules!?

Ever wanted to call a module directly, or index it?  Or just sick of seeing
`from foo import foo` in your examples?

Give your module the awesome power of an object, or maybe just save a
little typing, with `xmod`.

`xmod` is a tiny library that extends a module to do things that normally
only a class could do - handy for modules that "just do one thing".

EXAMPLE: Make a module callable as a function

.. code-block:: python

    # In your_module.py
    import xmod

    @xmod
    def a_function():
        return 'HERE!!'


    # Test at the command line
    >>> import your_module
    >>> your_module()
    HERE!!


EXAMPLE: Make a module look like an object

.. code-block:: python

    # In your_module.py
    import xmod

    xmod(list(), __name__)

    # Test at the command line
    >>> import your_module
    >>> assert your_module == []
    >>> your_module.extend(range(3))
    >>> print(your_module)
    [0, 1, 2]
"""
__all__ = ('xmod',)

import functools
import sys

__version__ = '1.2.1'

OMIT = {
    '__class__',
    '__getattr__',
    '__getattribute__',
    '__init__',
    '__init_subclass__',
    '__new__',
    '__setattr__',
}

EXTENSION_ATTRIBUTE = '_xmod_extension'
WRAPPED_ATTRIBUTE = '_xmod_wrapped'


def xmod(
    extension=None, name=None, full=None, props=None, omit=None, mutable=False
):
    """
    Extend the system module at `name` with any Python object.

    The original module is replaced in `sys.modules` by a proxy class
    which delegates attributes to the original module, and then adds
    attributes from the extension.

    In the most common use case, the extension is a callable and only the
    `__call__` method is delegated, so `xmod` can also be used as a
    decorator, both with and without parameters.

    ARGUMENTS
      extension
        The object whose methods and properties extend the namespace.
        This includes magic methods like __call__ and __getitem__.

      name
        The name of this symbol in `sys.modules`.  If this is `None`
        then `xmod` will use `extension.__module__`.

        This only needs to be be set if `extension` is _not_ a function or
        class defined in the module that's being extended.

        If the `name` argument is given, it should almost certainly be
        `__name__`.

      full
        If `False`, just add extension as a callable.

        If `True`, extend the module with all members of `extension`.

        If `None`, the default, add the extension if it's a callable, otherwise
        extend the module with all members of `extension`.

      mutable:
        If `True`, the attributes on the proxy are mutable and write through to
        the underlying module.  If `False`, the default, attributes on the
        proxy cannot be changed.

      omit
        A list of methods _not_ to delegate from the proxy to the extension.

        If `omit` is None, it defaults to `xmod.OMIT`, which seems to
        work well.
    """
    if extension is None:
        # It's a decorator with properties
        return functools.partial(
            xmod, name=name, full=full, props=props, omit=omit, mutable=mutable
        )

    def method(f):
        @functools.wraps(f)
        def wrapped(self, *args, **kwargs):
            return f(*args, **kwargs)

        return wrapped

    def mutator(f):
        def fail(*_):
            raise TypeError('Class is immutable')

        return method(f) if mutable else fail

    def prop(k):
        return property(
            method(lambda: getattr(extension, k)),
            mutator(lambda v: setattr(extension, k, v)),
            mutator(lambda: delattr(extension, k)),
        )

    name = extension.__module__ if name is None else name
    module = sys.modules[name]
    members = {
        WRAPPED_ATTRIBUTE: module,
        '__getattr__': method(module.__getattribute__),
        '__setattr__': mutator(module.__setattr__),
        '__delattr__': mutator(module.__delattr__),
        '__doc__': getattr(module, '__doc__'),
    }

    if callable(extension):
        members['__call__'] = method(extension)
        members[EXTENSION_ATTRIBUTE] = staticmethod(extension)

    elif full is False:
        raise ValueError('extension must be callable if full is False')

    else:
        members[EXTENSION_ATTRIBUTE] = extension
        full = True

    omit = OMIT if omit is None else set(omit)
    for a in dir(extension) if full else ():
        if a not in omit:
            value = getattr(extension, a)
            is_magic = a.startswith('__') and callable(value)
            members[a] = method(value) if is_magic else prop(a)

    def directory(self):
        return sorted(set(members).union(dir(module)))

    members['__dir__'] = directory

    proxy_class = type(name, (object,), members)
    sys.modules[name] = proxy_class()
    return extension


xmod(xmod)
