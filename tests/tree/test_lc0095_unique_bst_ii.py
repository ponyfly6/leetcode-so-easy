from problems.tree.lc0095_unique_bst_ii import Solution


def tree_to_list(root):
    """Convert tree to level-order list for comparison."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class TestLc0095UniqueBstII:
    def setup_method(self):
        self.sol = Solution()

    def test_n3(self):
        trees = self.sol.generate_trees(3)
        assert len(trees) == 5

    def test_n1(self):
        trees = self.sol.generate_trees(1)
        assert len(trees) == 1
        assert trees[0].val == 1

    def test_n0(self):
        trees = self.sol.generate_trees(0)
        assert trees == []

    def test_n2(self):
        trees = self.sol.generate_trees(2)
        assert len(trees) == 2
