from problems.binary_search.lc0069_sqrtx import Solution


class TestLc0069Sqrtx:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        assert self.sol.my_sqrt(4) == 2

    def test_non_perfect_square(self):
        assert self.sol.my_sqrt(8) == 2

    def test_zero(self):
        assert self.sol.my_sqrt(0) == 0

    def test_one(self):
        assert self.sol.my_sqrt(1) == 1

    def test_large(self):
        assert self.sol.my_sqrt(2147483647) == 46340

    def test_perfect_square_large(self):
        assert self.sol.my_sqrt(100) == 10
