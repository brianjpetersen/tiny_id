# standard libraries
import sys
import datetime
# third party libraries
pass
# podimetrics libraries
from . import (corpus, random)


def stringify_int(i, corpus=corpus.legible):
    base = len(corpus)
    s = ''
    while i != 0:
        i, indx = divmod(i, base)
        s = corpus[indx] + s
    return s

PYTHON_VERSION = sys.version_info[:2]
if PYTHON_VERSION >= (3, 0):
    MIN_DATETIME = datetime.datetime.min
else:
    MIN_DATETIME = datetime.datetime(1900, 1, 1)

MIN_STRINGIFIED_DATETIME = stringify_int(int(MIN_DATETIME.strftime('%Y%m%d%H%M%S%f')))
MAX_STRINGIFIED_DATETIME = stringify_int(int(datetime.datetime.max.strftime('%Y%m%d%H%M%S%f')))


def generate(when=None, random_length=0, corpus=corpus.legible, dense=True,
             precision='microsecond'):
    if when is None:
        when = datetime.datetime.utcnow()
    if precision == 'microsecond':
        upper_bound = 20
    elif precision == 'millisecond':
        upper_bound = 20 - 3
    elif precision == 'second':
        upper_bound = 20 - 6
    elif precision == 'minute':
        upper_bound = 20 - 8
    elif precision == 'hour':
        upper_bound = 20 - 10
    elif precision == 'day':
        upper_bound = 20 - 12
    elif precision == 'month':
        upper_bound = 20 - 14
    elif precision == 'year':
        upper_bound = 20 - 16
    else:
        raise ValueError('Precision must be one of microsecond, millisecond, \
                          second, minute, hour, day, month, or year.')
    random_id = random.generate(random_length, corpus)
    when = when.strftime('%Y%m%d%H%M%S%f')[:upper_bound]
    if not dense:
        when = stringify_int(int(when)).rjust(len(MAX_STRINGIFIED_DATETIME), min(corpus))
    return when + random_id
