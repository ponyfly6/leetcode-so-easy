class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    


from typing import List, Optional

"""
两种解法：
    1 递归
    2 动态规划 （递归 + 记忆化）
"""

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        """
        main function
        """
        if n == 0:
            return []
        return self._generate(1, n)

    def _generate(self, start: int, end: int) -> List[Optional[TreeNode]]:
        if start > end:
            return [None]

        all_trees = []

        for i in range(start, end + 1):         # 笛卡尔积
            left_trees = self._generate(start, i - 1)
            right_trees = self._generate(i + 1, end)

            for left_tree in left_trees:
                for right_tree in right_trees: 
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)

        return all_trees
    
# --- 如何使用 ---
# 创建一个 Solution 实例
solver = Solution()

# 调用方法，例如 n = 3
n = 3
result_trees = solver.generateTrees(n)

# 打印结果树的数量
print(f"对于 n = {n}, 共生成了 {len(result_trees)} 种不同的二叉搜索树。")

# 为了验证，我们可以简单打印一下每个树的根节点值
# 注意：要完整地看到树的结构，需要实现一个树的遍历打印函数（如层序遍历）
print("所有树的根节点值分别是:")
for tree in result_trees:
    if tree:
        print(tree.val)



