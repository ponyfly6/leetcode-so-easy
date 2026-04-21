"""
Tests for LeetCode 333. Largest BST Subtree
"""
from problems.tree.lc0333_largest_bst_subtree import Solution, TreeNode


def build_tree(values):
    """Build tree from level-order list."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestLc0333LargestBstSubtree:
    def setup_method(self):
        self.sol = Solution()

    def test_example1(self):
        # Tree:
        #       10
        #      /  \
        #     5   15
        #    / \    \
        #   1   8   7
        root = build_tree([10, 5, 15, 1, 8, None, 7])
        assert self.sol.largestBSTSubtree(root) == 3  # BST: [5,1,8]

    def test_example2(self):
        # Tree:
        #        0
        #         \
        #          1
        #         /
        #        2
        #       /
        #      3
        root = build_tree([0, None, 1, None, 2, None, 3])
        # This is a valid BST since it's a chain of increasing values
        assert self.sol.largestBSTSubtree(root) == 4

    def test_empty_tree(self):
        assert self.sol.largestBSTSubtree(None) == 0

    def test_single_node(self):
        root = TreeNode(1)
        assert self.sol.largestBSTSubtree(root) == 1

    def test_entire_tree_is_bst(self):
        # Valid BST
        #     5
        #    / \
        #   3   7
        root = build_tree([5, 3, 7])
        assert self.sol.largestBSTSubtree(root) == 3

    def test_no_valid_bst_subtree(self):
        # Tree:
        #     1
        #    / \
        #   2   3
        # left child (2) > root (1), so not a BST
        root = build_tree([1, 2, 3])
        assert self.sol.largestBSTSubtree(root) == 1

    def test_left_child_only_invalid(self):
        # Tree:
        #     1
        #    /
        #   2
        # 2 > 1, so not a valid BST
        root = build_tree([1, 2])
        assert self.sol.largestBSTSubtree(root) == 1

    def test_right_child_only(self):
        # Tree:
        #     1
        #      \
        #       2
        # 2 > 1, valid BST
        root = build_tree([1, None, 2])
        assert self.sol.largestBSTSubtree(root) == 2

    def test_nested_bst(self):
        # Tree:
        #        5
        #       / \
        #      1   4
        #         / \
        #        3   6
        # Root 5 is not BST because right_min=3, 5<3 is false
        # BST is subtree rooted at 4: [4,3,6], size 3
        root = build_tree([5, 1, 4, None, None, 3, 6])
        assert self.sol.largestBSTSubtree(root) == 3

    def test_large_valid_bst(self):
        # Complete valid BST
        #        5
        #      /   \
        #     3     7
        #    / \   / \
        #   1   4 6   8
        root = build_tree([5, 3, 7, 1, 4, 6, 8])
        assert self.sol.largestBSTSubtree(root) == 7
