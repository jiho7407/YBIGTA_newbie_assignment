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
    TC = int(input())
    for tc in range(TC):
        N, M = map(int, input().split())
        ST: SegmentTree[int, int] = SegmentTree(
            data = [0 for _ in range(M)] + [1 for _ in range(N)],
            pull = lambda a, b: a + b,
            conv = lambda x: x,
            default = 0
        )
        idxs = [(M + i) for i in range(N)]

        query = list(map(int, input().split()))
        topidx = M-1
        for q in query:
            q -= 1
            pos = idxs[q]
            print(ST.query(0, pos-1), end=' ')
            ST.update(pos, 0)
            ST.update(topidx, 1)
            idxs[q] = topidx
            topidx -= 1
        print()


if __name__ == "__main__":
    main()