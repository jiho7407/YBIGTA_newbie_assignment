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


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    input = sys.stdin.readline
    Q = int(input())
    ST: SegmentTree[int, int] = SegmentTree(
        data=[0 for _ in range(1000001)],
        pull=lambda a, b: a + b,
        conv=lambda x: x,
        default=0,
    )
    for _ in range(Q):
        op = list(map(int, input().split()))
        if op[0] == 1:
            ok, ng = 1000000, 0
            while ok - ng > 1:
                mid = (ok + ng) >> 1
                if ST.query(0, mid) >= op[1]:
                    ok = mid
                else:
                    ng = mid
            print(ok)
            ST.update(ok, ST.query(ok, ok) - 1)
        else:
            B, C = op[1], op[2]
            val = ST.query(B, B)
            ST.update(B, val + C)


if __name__ == "__main__":
    main()