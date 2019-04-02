from numpy.random import RandomState
from .types import NoneParam
from .types import ObjectParam
from .types import IntParam
from .types import UnionParam
import baysian
from datetime import datetime

def RandomStateParam():
    return UnionParam(NoneParam(), IntParam(), ObjectParam(RandomState))


def BaysianInit():
    def __init__(self,baysian.calc):
        return datetime.time()+""+self.baysian.calc.props()

        