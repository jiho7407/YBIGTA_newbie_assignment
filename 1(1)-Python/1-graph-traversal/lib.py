from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화
        n: 정점의 개수 (1번부터 n번까지)
        """
        self.n = n
        self.links: list[list[int]] = [[] for _ in range(n + 1)]

    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        인접 리스트 방식 사용
        """
        self.links[u].append(v)
        self.links[v].append(u)
    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색 (DFS)
        
        구현 방법 선택:
        1. 재귀 방식: 함수 내부에서 재귀 함수 정의하여 구현
        2. 스택 방식: 명시적 스택을 사용하여 반복문으로 구현
        """
        # ret = []
        # def _dfs(cur: int, par: int):
        #     ret.append(cur)
        #     for nxt in sorted(self.links[cur]):
        #         if nxt == par:
        #             continue
        #         _dfs(nxt, cur)
        # _dfs(start, -1)
        # return ret
        # 스택 구현 -> RecursionError

        ret = []
        visited = [False] * (self.n + 1)
        stk = [start]

        while stk:
            cur = stk.pop()
            if visited[cur]:
                continue
            visited[cur] = True
            ret.append(cur)
            for nxt in sorted(self.links[cur], reverse=True):
                if visited[nxt]:
                    continue
                stk.append(nxt)
        return ret
    
    def bfs(self, start: int) -> list[int]:
        """
        너비 우선 탐색 (BFS)
        큐를 사용하여 구현
        """
        ret = []
        visited = [False] * (self.n + 1)
        Q: deque[int] = deque()
        Q.append(start)
        visited[start] = True

        while Q:
            cur = Q.popleft()
            ret.append(cur)
            for nxt in sorted(self.links[cur]):
                if visited[nxt]:
                    continue
                visited[nxt] = True
                Q.append(nxt)

        return ret
    
    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))
