# standard libraries
import os
# third party libraries
pass
# first party libraries
from . import (random, temporal, )

_where = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(_where, '..', 'VERSION'), 'rb') as f:
    __version__ = f.read()