#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
116. 填充每个节点的下一个右侧节点指针
a. BFS
b. BFS-DFS
c. 使用已建立的 next 指针.
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
        方法：使用已建立的 next 指针.
        (0)每次将指针指向这一层最左边的位置
        (1) 连接1: 连接同一个父节点的两个子节点。它们可以通过同一个节点直接访问到。
        (2) 连接2: 在不同父亲的子节点之间建立连接: 第 N 层节点之间建立 next 指针后，再建立第 N+1 层节点的 next 指针。
        """
        if not root:
            return root
        # leftmost 是最左边的节点,从根节点开始
        leftmost = root
        while leftmost.left:
            # 遍历上面一层节点组织成的链表，为下一层的节点更新 next 指针
            up_head = leftmost
            while up_head:
                # 连接1: 连接同一个父节点的两个子节点
                up_head.left.next = up_head.right
                # 连接2: 在不同父亲的子节点之间建立连接
                if up_head.next:
                    up_head.right.next = up_head.next.left
                # 指针向后移动
                up_head = up_head.next
            leftmost = leftmost.left
        return root

    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        BFS: 遍历时记录每一层节点的个数。
        BFS遍历时，出队不一定只是出一次！！！
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
