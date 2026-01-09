from lib import SegmentTree
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