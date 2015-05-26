valuedispatch
=============

[singledispatch][]-like API but dispatches value instead of type.

[singledispatch]: https://docs.python.org/3/library/functools.html#functools.singledispatch

[![Build Status]
(https://travis-ci.org/what-studio/valuedispatch.svg)]
(https://travis-ci.org/what-studio/valuedispatch)
[![Coverage Status]
(https://img.shields.io/coveralls/what-studio/valuedispatch.svg)]
(https://coveralls.io/r/what-studio/valuedispatch)

```python
@valuedispatch
def encode(encoding, text):
    return text.encode(encoding)

@encode.register('base32')
def encode_base32(encoding, text):
    return base64.b32encode(text.encode('utf-8'))

encode('utf-8', u'Hello, world')
encode('base32', u'Hello, world')
```
