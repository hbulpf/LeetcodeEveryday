#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
116. 填充每个节点的下一个右侧节点指针
@Time : 2022/1/16 23:37
@Author: RunAtWorld
@File: 0116_M_populatingNextRightPointers.py
"""

# Definition for a Node.
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        BFS: 遍历时记录每一层节点的个数
        """
        if not root:
            return root
        que = collections.deque([root])
        while que:
            level_size = len(que)
            for i in range(level_size):
                # 这里每次都要更新node,同时 deque是个数组, que[0]可以取到头元素
                node = que.popleft()
                if i < level_size - 1:
                    node.next = que[0]
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root

    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        DFS: 将每层的节点都放到 List 中。最后逐层遍历List
        """
        if not root:
            return root
        res_list = list()

        def dfs(node, level):
            if not node:
                return
            if level >= len(res_list):
                res = [node]
                res_list.append(res)
            else:
                res_list[level].append(node)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        for same_level in res_list:
            for i in range(len(same_level) - 1):
                same_level[i].next = same_level[i + 1]
        return root
