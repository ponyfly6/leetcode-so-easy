from problems.backtracking.lc0140_word_break_ii import Solution


class TestLc0140WordBreakII:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        result = self.sol.word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        assert sorted(result) == sorted(["cats and dog", "cat sand dog"])

    def test_pineapple(self):
        result = self.sol.word_break(
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
        )
        expected = [
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple",
        ]
        assert sorted(result) == sorted(expected)

    def test_no_solution(self):
        result = self.sol.word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
        assert result == []

    def test_single_word(self):
        result = self.sol.word_break("apple", ["apple"])
        assert result == ["apple"]
