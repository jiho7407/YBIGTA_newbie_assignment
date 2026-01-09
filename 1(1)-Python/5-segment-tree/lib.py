from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    def __init__(self, data: list[U], pull: Callable[[T, T], T], conv: Callable[[U], T], default: T) -> None:
        self.n = len(data)
        self.sz = 1
        self.pull = pull
        self.conv = conv
        self.default = default
        while self.sz < self.n:
            self.sz *= 2
        self.tree: list[T] = [default] * (2 * self.sz)
        for i in range(self.n):
            self.tree[self.sz + i] = conv(data[i])
        for i in range(self.sz - 1, 0, -1):
            self.tree[i] = pull(self.tree[i << 1], self.tree[(i << 1) | 1])
    
    def update(self, i: int, node: U) -> None:
        i += self.sz
        self.tree[i] = self.conv(node)
        while i > 1:
            i >>= 1
            self.tree[i] = self.pull(self.tree[i << 1], self.tree[(i << 1) | 1])
    
    def query(self, l: int, r: int) -> T:
        L = l + self.sz
        R = r + self.sz + 1
        ret = self.default
        while L < R:
            if L & 1:
                ret = self.pull(ret, self.tree[L])
                L += 1
            if R & 1:
                R -= 1
                ret = self.pull(ret, self.tree[R])
            L >>= 1
            R >>= 1
        return ret