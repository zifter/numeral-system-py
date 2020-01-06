import os
import sys
sys.path.insert(0, os.path.abspath('./src'))

from setuptools import setup

import numeral_system


setup(
    name=numeral_system.__full_name__,
    version=numeral_system.__version__,
    description=numeral_system.__doc__.strip(),  # https://github.com/pypa/twine/issues/522
    author=numeral_system.__author__,
    author_email=numeral_system.__author_email__,
)
