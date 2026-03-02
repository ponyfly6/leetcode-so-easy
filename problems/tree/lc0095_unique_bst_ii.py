"""
LeetCode 95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/

Difficulty: Medium | Priority: P1 | Topic: tree, backtracking

## 思路
- 核心不变量：对于 [start, end] 区间，每个值 i 都可以作为根节点
- 左子树由 [start, i-1] 递归生成，右子树由 [i+1, end] 递归生成
- 笛卡尔积组合所有左右子树

## 复杂度
- Time: O(4^n / n^(3/2))  — 第 n 个 Catalan 数
- Space: O(4^n / n^(3/2))

## 边界条件
- n = 0 -> []
- n = 1 -> [TreeNode(1)]
- start > end -> [None]（空子树）

## 常见 Bug 审计
1. base case 返回 [None] 而不是 []，否则笛卡尔积无法生成
2. 每次循环必须创建新的 TreeNode（不能复用引用）
3. range(start, end+1) 别漏 +1
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self._generate(1, n)

    def _generate(self, start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]

        all_trees = []

        for i in range(start, end + 1):
            left_trees = self._generate(start, i - 1)
            right_trees = self._generate(i + 1, end)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)

        return all_trees
