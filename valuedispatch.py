# -*- coding: utf-8 -*-
"""
   valuedispatch
   ~~~~~~~~~~~~~

   :mod:`valuedispatch`-like API but dispatches value instead of type.

   :copyright: (c) 2015 by What! Studio
   :license: BSD, see LICENSE for more details.
"""
from functools import update_wrapper


__version__ = '0.0.1'
__all__ = ['valuedispatch']


# Import or define :class:`MappingProxyType`.
try:
    from singledispatch_helpers import MappingProxyType
except ImportError:
    try:
        from collections import UserDict
    except ImportError:
        from UserDict import UserDict
    class MappingProxyType(UserDict):
        def __init__(self, data):
            UserDict.__init__(self)
            self.data = data


def valuedispatch(func):
    """Decorates a function to dispatch handler of the value of the first
    argument.
    """
    registry = {}
    def dispatch(value):
        return registry.get(value, func)
    def register(value, func=None):
        if func is None:
            return lambda f: register(value, f)
        registry[value] = func
        return func
    def wrapper(*args, **kw):
        return dispatch(args[0])(*args, **kw)
    wrapper.register = register
    wrapper.dispatch = dispatch
    wrapper.registry = MappingProxyType(registry)
    update_wrapper(wrapper, func)
    return wrapper
