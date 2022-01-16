#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
733. 图像渲染
用两种方法
a. BFS:
b. DFS: 非递归和递归方法
@Time : 2022/1/16 00:02
@Author: RunAtWorld
@File: 0733_L_floodFill.py
"""
import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        DFS方法: 递归方法
        """
        len_row = len(image)
        len_col = len(image[0])
        initColor = image[sr][sc]
        if initColor == newColor:
            return image

        def dfs(x: int, y: int):
            image[x][y] = newColor
            for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                if 0 <= nx < len_row and 0 <= ny < len_col and image[nx][ny] == initColor:
                    dfs(nx, ny)

        dfs(sr, sc)
        return image

    def floodFill3(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        DFS方法: 非递归方法
        """
        len_row = len(image)
        len_col = len(image[0])
        initColor = image[sr][sc]
        if initColor == newColor:
            return image
        stack = collections.deque([(sr, sc)])
        while stack:
            x, y = stack.pop()
            if image[x][y] == initColor:
                image[x][y] = newColor
                for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < len_row and 0 <= ny < len_col and image[nx][ny] == initColor:
                        stack.append((nx, ny))
        return image

    def floodFill2(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        用BFS方法,但是对方法1进行改进
        注意:
        a.BFS遍历时，当前位置颜色只有与initColor相同才加入队列。遍历时不用 if 判断
        b.如果考虑 newColor 和 initColor 相同的情况,直接返回
        c.使用deque即可当栈也可当队列用
        """
        len_row = len(image)
        len_col = len(image[0])
        initColor = image[sr][sc]
        if initColor == newColor:
            return image
        que = collections.deque([(sr, sc)])
        que.append((sr, sc))
        while que:
            x, y = que.popleft()
            if image[x][y] == initColor:
                image[x][y] = newColor
                for nx, ny in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < len_row and 0 <= ny < len_col and image[nx][ny] == initColor:
                        que.append((nx, ny))
        return image

    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        用BFS方法
        注意:
        a.BFS遍历时，当前位置颜色只有与initColor相同才加入队列
        b.如果考虑 newColor 和 initColor 相同的情况，这里用了一个访问矩阵去判断
        """
        len_row = len(image)
        len_col = len(image[0])
        initColor = image[sr][sc]
        visited = [[False] * len_col for _ in range(len_row)]
        que = list()
        que.append((sr, sc))
        while que:
            row, col = que.pop(0)
            if image[row][col] == initColor:
                image[row][col] = newColor
                visited[row][col] = True
                if col > 0 and not visited[row][col - 1] and image[row][col - 1] == initColor:
                    que.append((row, col - 1))
                if col < len_col - 1 and not visited[row][col + 1] and image[row][col + 1] == initColor:
                    que.append((row, col + 1))
                if row > 0 and not visited[row - 1][col] and image[row - 1][col] == initColor:
                    que.append((row - 1, col))
                if row < len_row - 1 and not visited[row + 1][col] and image[row + 1][col] == initColor:
                    que.append((row + 1, col))
        return image


if __name__ == '__main__':
    solution = Solution()

    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    # 输出: [[2,2,2],[2,2,0],[2,0,1]]
    print(solution.floodFill(image, sr, sc, newColor))

    image = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sr = 1
    sc = 1
    newColor = 2
    print(solution.floodFill(image, sr, sc, newColor))

    image = [[0, 0, 0], [0, 1, 1]]
    sr = 1
    sc = 1
    newColor = 1
    print(solution.floodFill(image, sr, sc, newColor))
