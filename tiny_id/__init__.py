# standard libraries
import os
# third party libraries
pass
# first party libraries
from . import (_random, temporal, )



__where__ = os.path.dirname(os.path.abspath(__file__))
__all__ = ('__version__', '__where__', 'random', 'temporal', )


with open(os.path.join(__where__, '..', 'VERSION'), 'rb') as f:
    __version__ = f.read()
    

random = _random