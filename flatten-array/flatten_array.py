from collections.abc import Iterable

def flat_list(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

def flatten(iterable):
    return [value for value in flat_list(iterable) if value is not None]
