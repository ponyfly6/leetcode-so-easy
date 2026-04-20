from __future__ import annotations

"""
LeetCode 894. All Possible Full Binary Trees
https://leetcode.com/problems/all-possible-full-binary-trees/

Difficulty: Medium | Priority: P1 | Topic: tree, backtracking

## 思路
- 核心不变量：满二叉树节点数必须为奇数
- 递归拆分：根节点占 1 个，左子树 l 个（奇数），右子树 n-l-1 个
- 记忆化避免重复计算

## 复杂度
- Time: O(2^(n/2))  — Catalan 数级别
- Space: O(2^(n/2))

## 边界条件
- n 为偶数 -> []
- n = 1 -> 单节点树

## 常见 Bug 审计
1. 忘记 n 为偶数时直接返回空
2. 左子树遍历步长必须为 2（保持奇数）
3. 记忆化时要存结果引用，注意树节点共享
"""



class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.memo: dict[int, list[TreeNode | None]] = {
            1: [TreeNode(0)]
        }

    def all_possible_fbt(self, n: int) -> list[TreeNode | None]:
        if n in self.memo:
            return self.memo[n]

        if n % 2 == 0:
            return []

        all_trees = []

        for left_size in range(1, n, 2):
            right_size = n - left_size - 1
            left_trees = self.all_possible_fbt(left_size)
            right_trees = self.all_possible_fbt(right_size)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)

        self.memo[n] = all_trees
        return all_trees
