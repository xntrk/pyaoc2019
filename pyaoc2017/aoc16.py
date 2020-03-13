from itertools import count
from typing import List
import numpy as np

from cytoolz.itertoolz import first, take
import pyaoc2019.utils as U

__author__ = 'acushner'


def _parse_instruction(inst):
    return first(inst), inst[1:].split('/')


starting_layout = 'abcdefghijklmnop'


class Dance:
    def __init__(self):
        self.layout = list(starting_layout)
        self._cmds = self._init_cmds()

    def _init_cmds(self):
        return dict(
            s=self._spin,
            x=self._exchange,
            p=self._partner
        )

    def run(self, insts: List[str]):
        for cmd, args in map(_parse_instruction, insts):
            self._cmds[cmd](*args)

    def _spin(self, amount):
        amount = int(amount)
        self.layout = self.layout[-amount:] + self.layout[:-amount]

    def _exchange(self, a, b):
        """swap locations based on positions"""
        a, b = int(a), int(b)
        self.layout[a], self.layout[b] = self.layout[b], self.layout[a]

    def _partner(self, a, b):
        """swap locations based on names"""
        self._exchange(self.layout.index(a), self.layout.index(b))


def aoc16_a(insts):
    d = Dance()
    d.run(insts)
    return ''.join(d.layout)


def _create_start_end_map(ending_layout):
    return {i: ending_layout.index(c) for i, c in enumerate(starting_layout)}


def aoc16_b(insts):
    period, configurations = _find_period(insts)
    remaining = int(1e9 % period)
    return ''.join(configurations[remaining])


def _find_period(insts):
    d = Dance()
    sl = list(starting_layout)
    res = []
    for c in count(1):
        res.append(''.join(d.layout))
        d.run(insts)
        if sl == d.layout:
            return c, res


def __main():
    insts = first(U.read_file(16, 2017)).split(',')
    print(aoc16_a(insts))
    print(aoc16_b(insts))



if __name__ == '__main__':
    __main()
