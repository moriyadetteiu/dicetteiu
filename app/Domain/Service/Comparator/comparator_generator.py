from .AbstractComparator import AbstractComparator
from .GreaterThanComparator import GreaterThanComparator
from .GreaterEqualThanComparator import GreaterEqualThanComparator
from .LessThanComparator import LessThanComparator
from .LessEqualThanComparator import LessEqualThanComparator
from .NullComparator import NullComparator

def generate(method: str) -> AbstractComparator:
    if method == '>':
        return GreaterThanComparator()
    if method == '>=':
        return GreaterEqualThanComparator()
    if method == '<':
        return LessThanComparator()
    if method == '<=':
        return LessEqualThanComparator()

    return NullComparator()
