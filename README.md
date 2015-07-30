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

Written by [Heungsub Lee] at [What! Studio] in [Nexon], and
distributed under the [BSD 3-Clause] license.

[Heungsub Lee]: http://subl.ee/
[What! Studio]: https://github.com/what-studio
[Nexon]: http://nexon.com/
[BSD 3-Clause]: http://opensource.org/licenses/BSD-3-Clause
