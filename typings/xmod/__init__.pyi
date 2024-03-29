"""
This type stub file was generated by pyright.
"""

import functools
import sys
import typing as t

"""
# 🌱 Turn any object into a module 🌱

Callable modules!  Indexable modules!?

Ever wanted to call a module directly, or index it?  Or just sick of seeing
`from foo import foo` in your examples?

Give your module the awesome power of an object, or maybe just save a
little typing, with `xmod`.

`xmod` is a tiny library that lets a module to do things that normally
only a class could do - handy for modules that "just do one thing".

## Example: Make a module callable like a function!

    # In your_module.py
    import xmod

    @xmod
    def a_function():
        return 'HERE!!'


    # Test at the command line
    >>> import your_module
    >>> your_module()
    HERE!!

## Example: Make a module look like a list!?!

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
_OMIT = ...
_EXTENSION_ATTRIBUTE = ...
_WRAPPED_ATTRIBUTE = ...

def xmod(
    extension: t.Any = ...,
    name: t.Optional[str] = ...,
    full: t.Optional[bool] = ...,
    omit: t.Optional[t.Sequence[str]] = ...,
    mutable: bool = ...,
) -> t.Any:
    """
    Extend the system module at `name` with any Python object.

    The original module is replaced in `sys.modules` by a proxy class
    which delegates attributes to the original module, and then adds
    attributes from the extension.

    In the most common use case, the extension is a callable and only the
    `__call__` method is delegated, so `xmod` can also be used as a
    decorator, both with and without parameters.

    Args:
      extension: The object whose methods and properties extend the namespace.
        This includes magic methods like __call__ and __getitem__.

      name: The name of this symbol in `sys.modules`.  If this is `None`
        then `xmod` will use `extension.__module__`.

        This only needs to be be set if `extension` is _not_ a function or
        class defined in the module that's being extended.

        If the `name` argument is given, it should almost certainly be
        `__name__`.

      full: If `False`, just add extension as a callable.

        If `True`, extend the module with all members of `extension`.

        If `None`, the default, add the extension if it's a callable, otherwise
        extend the module with all members of `extension`.

      mutable: If `True`, the attributes on the proxy are mutable and write
        through to the underlying module.  If `False`, the default, attributes
        on the proxy cannot be changed.

      omit: A list of methods _not_ to delegate from the proxy to the extension

        If `omit` is None, it defaults to `xmod._OMIT`, which seems to
        work well.

    Returns:
        `extension`, the original item that got decorated
    """
    ...
