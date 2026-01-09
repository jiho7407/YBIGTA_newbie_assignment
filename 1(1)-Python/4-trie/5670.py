from lib import Trie
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