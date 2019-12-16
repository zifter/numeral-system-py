# numeral-system-py
Convert from one numeric system to other in python.
Supports following:
* roman numerals
* positional numerals (like binary, arabic (decimal), hexadecimal and others)

# Example of usage
## Roman
```python
>>> import numeral_system
>>> numeral_system.roman.encode(7)
'VII'
>>> numeral_system.roman.decode('XXII')
22
>>>
```

## Positional
```python
>>> import numeral_system
>>> numeral_system.positional.encode(42, 2)
'101010'
>>> numeral_system.positional.encode(12, 3)
'110'
>>> numeral_system.positional.decode(101, 2)
5
>>> numeral_system.positional.decode('AF', 16)
175
>>>
```

# Links
[![Release](https://img.shields.io/github/release/zifter/numeral-system-py.svg)][releases-url]
[![Supported versions](https://img.shields.io/pypi/pyversions/numeral-system.svg)][pypi-url]
[![Code Coverage](https://codecov.io/gh/zifter/numeral-system-py/branch/master/graph/badge.svg)][codecov-url]
[![Build status Appveyor](https://ci.appveyor.com/api/projects/status/github/zifter/numeral-system-py?branch=master&svg=true)][appveyor-url]
[![Build Status Travis CI](https://travis-ci.org/zifter/numeral-system-py.svg?branch=master)][travis-url]
[![Contact](https://img.shields.io/badge/telegram-write%20me-blue.svg)][telegram-url]

[releases-url]: https://github.com/zifter/numeral-system-py/releases
[codecov-url]: https://codecov.io/gh/zifter/numeral-system-py
[travis-url]: https://travis-ci.org/zifter/numeral-system-py
[appveyor-url]: https://ci.appveyor.com/project/zifter/numeral-system-py
[telegram-url]: https://t.me/zifter
[pypi-url]: https://pypi.org/project/numeral-system/