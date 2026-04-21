"""
LeetCode 333. Largest BST Subtree
https://leetcode.com/problems/largest-bst-subtree/

Difficulty: Medium | Priority: P1 | Topic: tree, DFS, BST

## 思路
- 后序遍历：自底向上传递信息
- 每个节点返回 (min, max, size, is_bst)
  - min: 子树最小值
  - max: 子树最大值
  - size: 最大BST子树的节点数
  - is_bst: 当前子树是否整体是BST
- BST 判定：左子树最大值 < 根 < 右子树最小值

## 复杂度
- Time: O(n) — 每个节点访问一次
- Space: O(h) — 递归栈深度，h为树高

## 边界条件
- 空树 -> 0
- 单节点 -> 1
- 非BST子树 -> 向下传递子树的BST size

## 常见 Bug 审计
1. 空子树返回特殊值 (inf, -inf, 0, True)
2. 全局变量 ans 需要在遍历中更新
3. BST 条件：左子树 < 根 < 右子树
"""
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        """
        Find the largest subtree in the binary tree that is a BST.
        Returns the number of nodes in the largest BST subtree.
        """
        self.ans = 0
        self._dfs(root)
        return self.ans

    def _dfs(self, node: Optional[TreeNode]) -> tuple[int, int, int, bool]:
        """
        Returns (min_val, max_val, bst_size, is_bst) for the subtree rooted at node.
        - min_val: minimum value in the subtree
        - max_val: maximum value in the subtree
        - bst_size: size of largest BST subtree
        - is_bst: whether this subtree is a BST
        """
        if not node:
            # 空子树：返回 (inf, -inf, 0, True)
            return (math.inf, -math.inf, 0, True)

        # 后序遍历
        left_min, left_max, left_size, left_bst = self._dfs(node.left)
        right_min, right_max, right_size, right_bst = self._dfs(node.right)

        # 检查当前节点是否能与左右子树形成 BST
        # BST 条件：左子树最大值 < 当前值 < 右子树最小值
        is_bst = left_bst and right_bst and left_max < node.val < right_min

        if is_bst:
            # 当前子树是 BST，大小 = 左子树节点 + 右子树节点 + 1
            bst_size = left_size + right_size + 1
            # 更新全局最大值
            self.ans = max(self.ans, bst_size)
            # 当前子树的 min/max
            min_val = min(left_min, node.val)
            max_val = max(right_max, node.val)
        else:
            # 当前不是 BST，返回子林中最大的 BST
            bst_size = max(left_size, right_size)
            self.ans = max(self.ans, bst_size)
            # 传递子树的 min/max（这里取左右子树的组合）
            min_val = min(left_min, node.val, right_min)
            max_val = max(left_max, node.val, right_max)

        return (min_val, max_val, bst_size, is_bst)
