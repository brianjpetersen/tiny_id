# standard libraries
import os
# third party libraries
pass
# first party libraries
from tiny_id import random

_where = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_where, '..', 'VERSION'), 'rb') as f:
    __version__ = f.read()