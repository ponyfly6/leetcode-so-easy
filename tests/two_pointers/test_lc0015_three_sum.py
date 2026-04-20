from problems.two_pointers.lc0015_three_sum import Solution


class TestLc0015ThreeSum:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        result = self.sol.three_sum([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert sorted(result) == sorted(expected)

    def test_all_zeros(self):
        assert self.sol.three_sum([0, 0, 0]) == [[0, 0, 0]]

    def test_no_solution(self):
        assert self.sol.three_sum([0, 1, 1]) == []

    def test_too_short(self):
        assert self.sol.three_sum([0]) == []

    def test_duplicates(self):
        result = self.sol.three_sum([-2, 0, 0, 2, 2])
        assert result == [[-2, 0, 2]]
