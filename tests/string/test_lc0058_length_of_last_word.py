from problems.string.lc0058_length_of_last_word import Solution


class TestLc0058LengthOfLastWord:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        assert self.sol.length_of_last_word("Hello World") == 5

    def test_trailing_spaces(self):
        assert self.sol.length_of_last_word("   fly me   to   the moon  ") == 4

    def test_single_word(self):
        assert self.sol.length_of_last_word("luffy") == 5

    def test_single_char(self):
        assert self.sol.length_of_last_word("a") == 1

    def test_spaces_between(self):
        assert self.sol.length_of_last_word("a b") == 1
