# -*- coding: utf-8 -*-
import base64

from six import b, u

from valuedispatch import valuedispatch


def test_singledispatch_like():
    @valuedispatch
    def foo(value):
        pass
    foo.register(1, foo)
    foo.register(2, foo)
    foo.dispatch(1) is foo
    foo.dispatch(2) is foo
    assert foo.registry[1] is foo
    assert foo.registry[2] is foo


def test_dispatch():
    @valuedispatch
    def encode(encoding, text):
        return text.encode(encoding)
    @encode.register('base32')
    def encode_base32(encoding, text):
        return base64.b32encode(text)
    assert encode('utf-8', u('Hello, world')) == b('Hello, world')
    assert encode('utf-16', u('Hello, world')) == b('\xff\xfeH\x00e\x00l\x00l'
                                                    '\x00o\x00,\x00 \x00w\x00o'
                                                    '\x00r\x00l\x00d\x00')
    assert encode('base32', u('Hello, world')) == b('JBSWY3DPFQQHO33SNRSA====')
