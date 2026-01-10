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



import sys


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = -1
        for child in trie[pointer].children:
            if trie[child].body == element:
                new_index = child
                break

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    input = sys.stdin.readline
    while True:
        try:
            N = int(input())
            trie: Trie = Trie()
            words = []
            for _ in range(N):
                word = input().strip()
                words.append(word)
                trie.push(word)
            total = 0
            for word in words:
                total += count(trie, word)
            print(f"{total/N:.2f}")
        except:
            return



if __name__ == "__main__":
    main()