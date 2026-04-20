from problems.backtracking.lc0093_restore_ip_addresses import Solution


class TestLc0093RestoreIpAddresses:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        result = self.sol.restore_ip_addresses("25525511135")
        assert sorted(result) == sorted(["255.255.11.135", "255.255.111.35"])

    def test_with_zeros(self):
        result = self.sol.restore_ip_addresses("0000")
        assert result == ["0.0.0.0"]

    def test_multiple_results(self):
        result = self.sol.restore_ip_addresses("101023")
        expected = ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
        assert sorted(result) == sorted(expected)

    def test_short_string(self):
        assert self.sol.restore_ip_addresses("1") == []

    def test_all_ones(self):
        result = self.sol.restore_ip_addresses("1111")
        assert result == ["1.1.1.1"]
