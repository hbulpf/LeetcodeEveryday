#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
617. 合并二叉树
@Time : 2022/1/16 20:20
@Author: RunAtWorld
@File: 0617_L_mergeTrees.py
"""

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1


    def mergeTrees_Error(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        BFS 错误
        """
        if not root1:
            return root2
        if not root2:
            return root1

        root = root1
        que1 = collections.deque([root1])
        que2 = collections.deque([root2])
        while que1 or que2:
            n1 = que1.popleft()
            n2 = que2.popleft()
            if not n1:
                n1 = TreeNode(0)
            if not n2:
                n2 = TreeNode(0)
            n1.val += n2.val
            que1.append(n1.left if n1.left else None)
            que1.append(n1.right if n1.right else None)
            que2.append(n2.right if n2.right else None)
            que2.append(n2.right if n2.right else None)
        return root

    def mergeTrees1(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        DFS
        """
        if not root1:
            return root2
        if not root2:
            return root1
        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

    def mergeTrees_Err(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        DFS 错误思路
        最开始的错误思路:
        a. 思维卡在考虑怎么构造新的二叉树，想偏了。
        b. 对递归的理解，还需提高！！！
        """
        root = TreeNode(0, None)
        if root1:
            root.val += root1.val
        if root2:
            root.val += root2.val

        def travel(root, root1, root2):
            if not root1 and not root2:
                return
            root.left = TreeNode(0, None)
            root.right = TreeNode(0, None)
            if root1:
                if root1.left:
                    root.left.val += root1.left.val
                if root1.right:
                    root.right.val += root1.right.val
            if root2:
                if root2.left:
                    root.left.val += root2.left.val
                if root2.right:
                    root.right.val += root2.right.val

            travel(root.left, root1.left, root2.left)
            travel(root.right, root2.right, root2.right)

        travel(root, root1, root2)
        return root


if __name__ == '__main__':
    r1n5 = TreeNode(5, None, None)
    r1n3 = TreeNode(3, r1n5, None)
    r1n2 = TreeNode(2, None, None)
    r1n1 = TreeNode(1, r1n3, r1n2)

    r2n4 = TreeNode(4, None, None)
    r2n7 = TreeNode(7, None, None)
    r2n1 = TreeNode(1, None, r2n4)
    r2n3 = TreeNode(3, None, r2n7)
    r2n2 = TreeNode(2, r2n1, r2n3)

    solution = Solution()
    solution.mergeTrees(r1n1, r2n2)
