#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
695. 岛屿的最大面积
a. DFS：递归遍历
b. 也可以用BFS
@Time : 2022/1/16 18:01
@Author: RunAtWorld
@File: 0695_M_maxAreaOfIsland.py
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS：递归遍历
        a. 对方法1进行改进，其实不需要访问过的矩阵，如果访问过，可以把该位置置为0
        b. 对于遍历面积类型的题目，可以用 (dx,dy) 表示遍历的方向,这看起来更加优雅
        """
        if not grid:
            return 0
        r_len, c_len = len(grid), len(grid[0])

        def dfs(x, y):
            if not grid[x][y]:
                return 0
            area = 1
            grid[x][y] = 0
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x + dx < r_len and 0 <= y + dy < c_len:
                    area += dfs(x + dx, y + dy)
            return area

        ans = 0
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j), ans)
        return ans

    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        """
        DFS：递归遍历
        """
        if not grid:
            return 0
        r_len, c_len = len(grid), len(grid[0])
        seen = [[False] * c_len for _ in range(r_len)]

        def dfs(x, y):
            if grid[x][y] == 0:
                return 0
            area = 1
            seen[x][y] = True
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= nx < r_len and 0 <= ny < c_len and not seen[nx][ny]:
                    area += dfs(nx, ny)
            return area

        ans = 0
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == 1:
                    ans = max(dfs(i, j), ans)
        return ans


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    solution = Solution()
    print(solution.maxAreaOfIsland(grid))
