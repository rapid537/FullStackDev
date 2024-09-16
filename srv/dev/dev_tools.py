import random


def key_generator(x=6):
    return str(
        random.randint(
            (10**(x - 1)),
            ((10 ** x) - 1),
        )
    )
