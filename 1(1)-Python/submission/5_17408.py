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


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: 'Pair', b: 'Pair') -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    input = sys.stdin.readline

    N = int(input())
    lst = list(map(int, input().split()))

    ST = SegmentTree(
        data = lst,
        pull = Pair.f_merge,
        conv = Pair.f_conv,
        default = Pair.default()
    )

    Q = int(input())
    for q in range(Q):
        op = list(map(int, input().split()))
        if op[0] == 1:
            i, v = op[1], op[2]
            i -= 1
            ST.update(i, v)
        else:
            L, R = op[1], op[2]
            L -= 1
            R -= 1
            print(ST.query(L, R).sum())


if __name__ == "__main__":
    main()