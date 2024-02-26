import os
import sys
import re
import io

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
  with io.open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as fp:
    requires = [r.strip() for r in fp.readlines()]
except FileNotFoundError:
    requires = [
      'six',
      'future-strings'
    ]
    
setup(
    name='Merkle_Tree_with_PIR',
    version=None,
    description='Merkle Tree for easier data verification and swapping tree nodes', 
    author='Huy Nguyen',
    author_email=None,
    python_requires='>=2.7',
    packages=find_packages(exclude=('tests',)),
    install_requires=requires,
)