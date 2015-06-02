# standard libraries
import random
import math
# third party libraries
pass
# podimetrics libraries
from . import corpus


def sample_with_replacement(population, number=1):
    for i in range(number):
        yield random.choice(population)


def bits_to_length(bits, corpus=corpus.legible):
    base = len(corpus)
    length = int(bits/math.log2(base) + 0.5)
    return length


def length_to_bits(length, corpus=corpus.legible):
    base = len(corpus)
    bits = int(length*math.log2(base))
    return bits


def collision_likelihood(length, number=1, corpus=corpus.legible):
    bits = length_to_bits(length, corpus)
    return 1.0 - math.exp(-0.5*number**2/2**bits)


def generate(length=22, corpus=corpus.legible):
    random_string = ''.join(sample_with_replacement(corpus, length))
    return random_string