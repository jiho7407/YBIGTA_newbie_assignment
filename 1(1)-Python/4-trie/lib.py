from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

        factorials = [1]
        for i in range(1, 3001):
            factorials.append((factorials[-1] * i) % 1000000007)
        self.factorials = factorials

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """

        cur = 0
        for val in seq:
            flag = False
            for child in self[cur].children:
                if self[child].body == val:
                    cur = child
                    flag = True
                    break
            if not flag:
                nxt = TrieNode(body=val)
                nxtidx = len(self)
                self[cur].children.append(nxtidx)
                self.append(nxt)
                cur = nxtidx
        self[cur].is_end = True

    def dfs(self, cur: int) -> int:
        """
        boj 3080, 아름다운 이름 규칙의 순서 수 정하기
        """
        cnt = len(self[cur].children)
        ret = 1

        for nxt in self[cur].children:
            ret *= self.dfs(nxt)
            ret %= 1000000007

        if self[cur].is_end:
            cnt += 1
        
        ret *= self.factorials[cnt]
        ret %= 1000000007
        return ret
