from lib import Trie
import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    sys.setrecursionlimit(3010)
    input = sys.stdin.readline
    N = int(input())
    trie: Trie = Trie()
    words = []
    for _ in range(N):
        word = input().strip()
        words.append(word)
    words.sort()

    def LCP(a: str, b: str) -> int:
        lcp = 0
        for x, y in zip(a, b):
            if x == y:
                lcp += 1
            else:
                break
        return lcp
    
    for i, word in enumerate(words):
        if i == 0 or i == N - 1:
            trie.push(word)
        else:
            val = max(LCP(word, words[i - 1]), LCP(word, words[i + 1]))
            trie.push(word[:val + 1])

    ans = trie.dfs(0)
    print(ans)


if __name__ == "__main__":
    main()