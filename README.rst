|Release| |Supported versions| |Code Coverage| |Build status Appveyor| |Build Status Travis CI| |Contact|

numeral-system-py
=================

Convert from one numeric system to other in python.

Supports following:

* roman numerals
* positional numerals (like binary, arabic (decimal), hexadecimal and others)

Example of usage
----------------
Roman
^^^^^
.. code:: python

    >>> import numeral_system
    >>> numeral_system.roman.encode(7)
    'VII'
    >>> numeral_system.roman.decode('XXII')
    22

Positional
^^^^^^^^^^
.. code:: python

    >>> import numeral_system
    >>> numeral_system.positional.encode(42, 2)
    '101010'
    >>> numeral_system.positional.encode(12, 3)
    '110'
    >>> numeral_system.positional.decode(101, 2)
    5
    >>> numeral_system.positional.decode('AF', 16)
    175

.. |Release| image:: https://img.shields.io/github/release/zifter/numeral-system-py.svg
   :target: https://github.com/zifter/numeral-system-py/releases
.. |Supported versions| image:: https://img.shields.io/pypi/pyversions/numeral-system.svg
   :target: https://pypi.org/project/numeral-system/
.. |Code Coverage| image:: https://codecov.io/gh/zifter/numeral-system-py/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/zifter/numeral-system-py
.. |Build status Appveyor| image:: https://ci.appveyor.com/api/projects/status/github/zifter/numeral-system-py?branch=master&svg=true
    :target: https://ci.appveyor.com/project/zifter/numeral-system-py
.. |Build Status Travis CI| image:: https://travis-ci.org/zifter/numeral-system-py.svg?branch=master
    :target: https://travis-ci.org/zifter/numeral-system-py
.. |Contact| image:: https://img.shields.io/badge/telegram-write%20me-blue.svg
    :target:  https://t.me/zifter
