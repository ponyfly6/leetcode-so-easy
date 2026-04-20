from problems.backtracking.lc0241_diff_ways_to_compute import Solution


class TestLc0241DiffWaysToCompute:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        result = self.sol.diff_ways_to_compute("2-1-1")
        assert sorted(result) == sorted([0, 2])

    def test_multiply(self):
        result = self.sol.diff_ways_to_compute("2*3-4*5")
        assert sorted(result) == sorted([-34, -14, -10, -10, 10])

    def test_single_number(self):
        assert self.sol.diff_ways_to_compute("3") == [3]

    def test_simple_add(self):
        assert self.sol.diff_ways_to_compute("1+1") == [2]
