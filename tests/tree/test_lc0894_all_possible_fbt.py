from problems.tree.lc0894_all_possible_fbt import Solution


class TestLc0894AllPossibleFbt:
    def setup_method(self):
        self.sol = Solution()

    def test_n7(self):
        result = self.sol.all_possible_fbt(7)
        assert len(result) == 5

    def test_n3(self):
        result = self.sol.all_possible_fbt(3)
        assert len(result) == 1

    def test_n1(self):
        result = self.sol.all_possible_fbt(1)
        assert len(result) == 1

    def test_even_returns_empty(self):
        assert self.sol.all_possible_fbt(2) == []
        assert self.sol.all_possible_fbt(4) == []

    def test_n5(self):
        result = self.sol.all_possible_fbt(5)
        assert len(result) == 2
