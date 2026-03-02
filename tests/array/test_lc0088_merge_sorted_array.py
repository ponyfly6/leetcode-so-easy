from problems.array.lc0088_merge_sorted_array import Solution


class TestLc0088MergeSortedArray:
    def setup_method(self):
        self.sol = Solution()

    def test_basic(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        self.sol.merge(nums1, 3, [2, 5, 6], 3)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_edge_nums2_empty(self):
        nums1 = [1]
        self.sol.merge(nums1, 1, [], 0)
        assert nums1 == [1]

    def test_edge_nums1_empty(self):
        nums1 = [0]
        self.sol.merge(nums1, 0, [1], 1)
        assert nums1 == [1]

    def test_all_nums2_smaller(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        self.sol.merge(nums1, 3, [1, 2, 3], 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_all_nums2_larger(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        self.sol.merge(nums1, 3, [4, 5, 6], 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]
