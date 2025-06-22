from typing import List, Optional, Dict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.memo: Dict[int, List[Optional[TreeNode]]] = {
            # 预制基础解： 1 个node只有一种情况
            1: [TreeNode(0)]
        }

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n in self.memo:
            return self.memo[n]
        
        if n % 2 == 0:
            return []
        
        all_trees = []

        # 左子树的node 数必须是奇数
        for l in range(1, n, 2):
            r = n - l - 1
            left_trees = self.allPossibleFBT(l)
            right_trees = self.allPossibleFBT(r)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)

        self.memo[n] = all_trees
        return all_trees


solver = Solution()
n = 7
result = solver.allPossibleFBT(n)
print(len(result))