from lib import SegmentTree
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